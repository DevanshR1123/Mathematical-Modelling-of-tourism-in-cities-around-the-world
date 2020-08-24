from functools import reduce

import folium as fl

from data import cities, hlocs, hnames, plocs, pnames

hclrs = []
pclrs = []

mp = fl.Map(location=[0, 0], zoom_start=2)

for city in cities:
    lats = [l[0] for l in hlocs[city]]
    lons = [l[1] for l in hlocs[city]]

    for i, l, n in zip(range(len(hnames[city])), hlocs[city], hnames[city]):
        fl.Marker(location=l, tooltip=f'{str(i+1)}. {n}', icon=fl.Icon(
            color='blue', icon_color='lightgray')).add_to(mp)

    for i, l, n in zip(range(len(pnames[city])), plocs[city], pnames[city]):
        fl.Marker(location=l, tooltip=f'{str(i+1)}. {n}', icon=fl.Icon(
            color='red', icon_color='lightgray')).add_to(mp)

mp.save('./locations_dist.html')
