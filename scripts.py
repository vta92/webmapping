import folium

#tiles basically tells us the way the map is presented/background
map = folium.Map(location = [10.4114, 107.1362], zoom_start = 6, \
tiles = 'Mapbox Bright')

#a layer/feature group; more organized. Turning layers on and off
feat_group = folium.FeatureGroup(name = "My Map")

for coordinate in [[10.04, 105.75],[10.4, 107.1]]:
#to add individual stuff on map, use add_child
    feat_group.add_child(folium.Marker(location = coordinate, \
    popup= str(coordinate), icon = folium.Icon(color = 'blue')))

map.add_child(feat_group)

map.save('Vietnam')
