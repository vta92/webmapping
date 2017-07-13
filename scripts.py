import folium

map = folium.Map(location = [10.4114, 107.1362], zoom_start = 6, \
tiles = 'Mapbox Bright')

map.save('vung_tau')
