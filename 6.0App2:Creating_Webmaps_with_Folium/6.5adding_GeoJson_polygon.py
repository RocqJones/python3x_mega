import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[40.798361, -111.857243], zoom_start=2)

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(
        str(el)+"m", parse_html=True), fill_color=color_producer(el), color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
"""
    - GeoJson method
    - style_function() expects 'lambda' value
    - POP - population in '.json' file
    - For contries with population less tha 10million will be colored green.
    - For those btwn 10 and 20 million be colored orange.
    - Those greater than 20m will be colored red 
"""
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {
             'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

# Adding layer control panel. Add this after adding feature group to the obj 'map'
map.add_child(folium.LayerControl())

map.save("Map5.html")
