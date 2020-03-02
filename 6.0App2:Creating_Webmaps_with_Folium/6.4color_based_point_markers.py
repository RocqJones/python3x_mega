import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")

# get latitudes and longitudes, and put them in a list
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"]) # list of elevations to set to popup

# color function will point different colors btwn markers based on size. 'el' will be parsed to 'elevation'
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    # btwn 1000 n 3000
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

# root map object
map = folium.Map(location=[40.798361, -111.857243], zoom_start=6)

# create a feature group
fg = folium.FeatureGroup(name="My Map")

# when you iterate through 2 lists use zip fun to set latitude against longitude
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup = folium.Popup(str(el)+"m",parse_html=True), icon=folium.Icon(color=color_producer(el))))

map.add_child(fg)

map.save("Map4.html")