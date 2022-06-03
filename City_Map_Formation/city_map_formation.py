# pandas and folium libraries should be installed
import folium
import pandas

# data of all cities and locations can be downloaded from https://simplemaps.com/data/world-cities
# after downloaded, worldcities.csv inside the .rar file should be extracted and put in the current working directory
data = pandas.read_csv("worldcities.csv", encoding="ISO-8859-1")

# below lits containes the values for each variable
country = list(data["country"])
city_name = list(data["city_ascii"])
lat = list(data["lat"])
lon = list(data["lng"])
population = list(data["population"])
city_status = list(data["capital"])

# this codes use folium library to create a map
world_map = folium.Map(location=[50, 50], zoom_start=3)
fg = folium.FeatureGroup(name="world_map")

html = """<h4>City information:</h4>
Name: %s
Population: %s
Status: %s
"""


# this function creates a map for only world (NOTE that very high computing power is needed to process this one)
def world_map_creator():
    for city, pop, status, latitude, longitute in zip(city_name, population, city_status,
                                                      lat, lon):
        print("\nMap is being made... Please wait...\n")
        iframe = folium.IFrame(html=html % (city, pop, status), width=200, height=100)
        fg.add_child(folium.Marker(location=[latitude, longitute],
                                   popup=folium.Popup(iframe),
                                   icon=folium.Icon(color="blue")))
    world_map.add_child(fg)
    world_map.save(f"map_of_World.html")
    print("\nA map containing the locations and information of all world cities is created and saved as "
          "'map_of_World.html' in your current direcotry")


# this function create a map with the cities of a country
def country_map_formation(country_name_input):
    input_value = country_name_input

    for country_name, city, pop, status, latitude, longitute in zip(country, city_name, population, city_status,
                                                                    lat, lon):
        iframe = folium.IFrame(html=html % (city, pop, status), width=200, height=100)
        if country_name.upper() == input_value.upper():
            # makes the tag of capital city in red
            if status == "primary":
                fg.add_child(folium.Marker(location=[latitude, longitute],
                                           popup=folium.Popup(iframe),
                                           icon=folium.Icon(color="red")))

            # makes the tag of non-capital city in blue
            else:
                fg.add_child(folium.Marker(location=[latitude, longitute],
                                           popup=folium.Popup(iframe),
                                           icon=folium.Icon(color="blue")))


# this is the main function and aks user to pun in the country or countries to create the map of
def map_creator():
    countries_list = []

    while True:
        input_value = input(
            "Which country's cities do you want to make a map of? (Put 'World' to see all cities of the world: ")

        if input_value.upper() == "WORLD":
            world_map_creator()
            break

        elif input_value.upper() not in list(c.upper() for c in country):
            print("\nSuch a country is not found. Please, put a valid country name written in English\n")
            continue

        else:
            print("\nMap is being made... Please wait...\n")
            country_map_formation(input_value)
            world_map.add_child(fg)
            print("Done!")
            countries_list.append(input_value)

            while True:
                if_add_more = input("\nDo you want to add another country's cities? (Y/N)\n")
                if if_add_more.upper() == "Y":
                    another_country = input("\nName the other country: ")
                    if another_country.upper() in list(c.upper() for c in country):
                        print("\nMap is being made... Please wait...\n")
                        country_map_formation(another_country)
                        print(f"\n{another_country.title()} is added")
                        world_map.add_child(fg)
                        countries_list.append(another_country)
                        continue
                    else:
                        print("\nSuch a country is not found. Please put a valid country name\n")
                        continue
                elif if_add_more.upper() == "N":
                    break
                else:
                    print("\nPleae put a valid answer")
                    continue
            print("\nYour map is created and saved in the current directory")

            conts_name = "_".join(countries_list)
            world_map.save(f"map_of_{conts_name}.html")
            break


# call the mail function
map_creator()
