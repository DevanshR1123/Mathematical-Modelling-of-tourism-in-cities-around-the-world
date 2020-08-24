from random import randint, random

from colored import attr, bg, fg, stylize
from pandas import DataFrame as df

from data import cities, hotels, places
from map_plot import map_path
from traveller import Traveller, distance

for city in cities:

    nhotels = len(hotels[city])
    nplaces = len(places[city])

    hotel_prob_table = [100/nhotels for i in range(nhotels)]
    places_prob_table = [[100/(nplaces-1)if i != j else 0 for j in range(nplaces)]
                         for i in range(nplaces)]
    hotels_prob_table = [[100/(nplaces) for j in range(nplaces)]
                         for i in range(nhotels)]

    tl = randint(12, 16)  # int(input('total travel time: '))
    hl = 2 + random()
    inc = .1
    trials = 10000  # int(input('number of trials: '))

    start = None
    path = []
    time = []

    for i in range(trials):
        Trv = Traveller()
        hotel_prob_table = Trv.choose_hotel(hotels[city], hotel_prob_table)
        hotels_prob_table = Trv.travel_h(
            hotels[city], places[city], hotels_prob_table)

        t = 0
        ttt = 0

        prev = hotels[city][Trv.get_start()]
        curr = places[city][Trv.get_location()]

        tt = distance(prev, curr)/16
        t += tt
        ttt += tt
        ts = 0
        hp = Trv.calc_hp(curr, ts)

        while hp > hl and t < tl:
            ts += inc
            t += inc
            hp = Trv.calc_hp(curr, ts)
        else:
            Trv.add_timestamp(ts)
            Trv.add_traveltime(tt)

        while t < tl:
            prev = places[city][Trv.get_location()]
            places_prob_table = Trv.travel(places[city], places_prob_table)
            curr = places[city][Trv.get_location()]
            tt = distance(prev, curr)/16
            t += tt
            ttt += tt
            ts = 0
            hp = Trv.calc_hp(curr, ts)

            while hp > hl and t < tl:
                ts += inc
                t += inc
                hp = Trv.calc_hp(curr, ts)
            else:
                Trv.add_timestamp(ts)
                Trv.add_traveltime(tt)
        else:
            path = Trv.get_path()
            start = Trv.get_start()
            time = Trv.get_time()

        if i == trials-1:
          ###########################################################
            print(stylize(hotels[city][start]['name'],
                          attr(1)+fg('#ff9933')+bg('black')))
          ###########################################################
            print(stylize(df(zip(
                map(lambda x: places[city][x]['name'], path),
                map(lambda x: round(x, 2), time),
                map(lambda x: round(x, 2), Trv.get_travel())
            ), index=range(1, len(path)+1),
                columns=['Location', 'Time Spent', 'Travel Time']),
                attr(21)+bg('black')))
          ###########################################################
            print(stylize(f'{ttt:.2f} hrs of Travel Time',
                          fg('#dd7a09')+attr(21)+bg('black')))

    map_path(start, path, time, city)
    print('─'*100)
