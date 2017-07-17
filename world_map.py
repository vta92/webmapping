import folium
import pandas as pd
import sys

'''This script only puts on map big cities that has population over 2 mil'''

df = pd.read_csv('world_cities.csv')
df = df[df['pop'] > 2000000]
#print(df)

lattitudes = list(df["lat"])
longitudes = list(df['lng'])
cities = list(df['city'])
pop = list(df['pop'])
countries = list(df['country'])

#print(len(lattitudes), len(longitudes), len(cities)
#initialize a map
map = folium.Map(location =[10.8231,106.6297], zoom_start= 6, tiles = "cartodbpositron")
fg = folium.FeatureGroup(name = 'My map')


#putting markers on the map
for i in range(len(cities)):
    fg.add_child(folium.Marker(location = [lattitudes[i], longitudes[i]],\
    popup=str(cities[i] + ", " + "Popution: " + str(pop[i]) + ", " "Country: " \
    + str(countries[i]))))

map.add_child(fg)

map.save('world_map')

exit()
