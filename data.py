import pandas as pd
from stat_funcs import normalise_range

cities = open('./data/cities.txt').read().splitlines()

places = {}
hotels = {}

for city in cities:

    hotels_data: pd.DataFrame = pd.read_excel('./data/hotels_data.xlsx', city)
    places_data: pd.DataFrame = pd.read_excel('./data/places_data.xlsx', city)

    hr = hotels_data['rating']
    htr = hotels_data['total_rating']
    hp = hotels_data['price']

    n_hotel_rating = normalise_range(hr, 0, 100)
    n_hotel_total_rating = normalise_range(htr, 0, 100)
    n_hotel_price = normalise_range(hp, 0, 100)

    pr = places_data['rating']
    ptr = places_data['total_rating']

    n_places_rating = normalise_range(pr, 0, 100)
    n_places_total_rating = normalise_range(ptr, 0, 100)

    hotels_data['n_rating'] = n_hotel_rating
    hotels_data['n_total_rating'] = n_hotel_total_rating
    places_data['n_rating'] = n_places_rating
    places_data['n_total_rating'] = n_places_total_rating
    hotels_data['n_price'] = n_hotel_price

    hotels[city] = list(hotels_data.to_dict(orient='index').values())
    places[city] = list(places_data.to_dict(orient='index').values())


plocs = {}
pnames = {}
hlocs = {}
hnames = {}


for city in cities:
    plocs[city] = [(p['lat'], p['lng'])for p in places[city]]
    pnames[city] = [p['name'] for p in places[city]]
    hlocs[city] = [(h['lat'], h['lng']) for h in hotels[city]]
    hnames[city] = [h['name'] for h in hotels[city]]
