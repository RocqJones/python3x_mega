import folium

# map object
map = folium.Map(location=[-3.401530, 38.555789], zoom_start=8)

# create a feature group
fg = folium.FeatureGroup(name="My Map")

# add elements to the object. Leaflet Marker is for JS with optional popup text.
# fg.add_child(folium.Marker(location=[-3.401530, 38.555789], popup="Marker location", icon=folium.Icon(color='green')))
# fg.add_child(folium.Marker(location=[-3.403629, 38.363485], popup="Marker location", icon=folium.Icon(color='orange')))

# use loops
list_of_coordinates = [[-3.401530, 38.555789],[-3.403629, 38.363485]]

for coordinates in list_of_coordinates:
    fg.add_child(folium.Marker(location=coordinates, popup="Marker location", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map2.html")