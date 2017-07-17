import folium
import pandas as pd
import sys
import csv

#saving the countries and number of cities that qualify pop requirement
#in csv file
def writer(country_city_cnt):
    with open('country_stats.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in country_city_cnt.items():
            writer.writerow([key,value])

#adding marker filter based on population's scalar quantities
def color_prod(population):
    if population < 3000000:
        return "blue"
    elif (population >= 3000000) and (population < 5000000):
        return "green"
    elif (population >= 5000000) and (population < 7000000):
        return "orange"
    else:
        return "red"



'''This script only puts on map big cities that has population over 2 mil'''
if __name__ =='__main__':

    df = pd.read_csv('world_cities.csv')
    df = df[df['pop'] > 2000000]
    #print(df)

    lattitudes = list(df["lat"])
    longitudes = list(df['lng'])
    cities = list(df['city'])
    pop = list(df['pop'])
    countries = list(df['country'])
    #this dict will store number of cities per country with >2mil pop
    country_city_cnt = dict()
    #print(len(lattitudes), len(longitudes), len(cities)

    #initialize a map
    map = folium.Map(location =[10.8231,106.6297], zoom_start= 6, tiles = "cartodbpositron")
    fg = folium.FeatureGroup(name = 'My map')


    #putting markers on the map
    for i in range(len(cities)):
        fg.add_child(folium.CircleMarker(location = [lattitudes[i], longitudes[i]],\
        radius = 10, popup=str(cities[i] + ", " + "Popution: " + str(pop[i]) + ", " "Country: " \
        + str(countries[i])), fill_color = color_prod(pop[i]), color = 'black', fill_opacity = 0.8))

        if countries[i] not in country_city_cnt:
            country_city_cnt[countries[i]] = 1
        else:
            country_city_cnt[countries[i]] += 1

    map.add_child(fg)
    map.save('world_map')
    #print(country_city_cnt)
    writer(country_city_cnt)

    exit()
