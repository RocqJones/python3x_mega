import folium
import pandas

# load data
data = pandas.read_csv("Volcanoes_USA.txt")
# data.columns

# get latitudes and longitudes, and put them in a list
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"]) # list of elevations to set to popup

# root map object
map = folium.Map(location=[40.798361, -111.857243], zoom_start=6)

# create a feature group
fg = folium.FeatureGroup(name="My Map")

# when you iterate through 2 lists use zip fun to set latitude against longitude
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup = folium.Popup(str(el)+"m",parse_html=True), icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map3.html")