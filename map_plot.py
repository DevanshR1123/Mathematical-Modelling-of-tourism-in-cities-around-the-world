import folium as fl
from data import cities, hlocs, hnames, plocs, pnames
from pandas import DataFrame as df


def map_path(start, path, time, city):

    lats = [l[0] for l in hlocs[city]]
    lons = [l[1] for l in hlocs[city]]

    latb = (max(lats)+.05, min(lats)-.05)
    lonb = (max(lons)+.05, min(lons)-.05)
    c = [sum(latb)/2, sum(lonb)/2]
    bb = [(latb[1], lonb[1]), (latb[0], lonb[0])]

    mp = fl.Map(location=c, zoom_start=18)
    mp.fit_bounds(bb)

    loc_path = list(map(lambda i: plocs[city][i], path))
    name_path = list(map(lambda i: pnames[city][i], path))

    fl.PolyLine(locations=[hlocs[city][start]]+loc_path).add_to(mp)
    fl.Marker(location=hlocs[city][start], tooltip='1. '+hnames[city][start], icon=fl.Icon(
        color='green', icon_color='lightgray')).add_to(mp)

    for i, l, n in zip(range(len(path)), loc_path, name_path):
        fl.Marker(location=l, tooltip=str(i+2)+'. '+n, icon=fl.Icon(
            color='red', icon_color='lightgray')).add_to(mp)

    open(f'./latest_path/{city}.html', 'w+').write(f'<h3>{hnames[city][start]}</h3>' +
                                                   df(zip(name_path, map(lambda x: f'{int(x//1)} hrs {int((x%1)*60)} mins', time)),
                                                      columns=['Location', 'Time spent'], index=range(1, len(path)+1)).to_html(border=0, classes='tbl') +
                                                   '<a href="https://github.com/DevanshR1123/Mathematical-Modelling-of-tourism-in-cities-around-the-world">View code on GitHub</a>',
                                                   )

    mp.save(f'./map/{city}.html')
