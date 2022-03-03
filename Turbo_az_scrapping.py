#Turbo.az scrapped

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://turbo.az/autos?page=5&q%5Bbarter%5D=0&q%5Bcurrency%5D=azn&q%5Bloan%5D=0&q%5Bmake%5D%5B%5D=41&q%5Bmodel%5D%5B%5D=970&q%5Bprice_from%5D=&q%5Bprice_to%5D=&q%5Bregion%5D%5B%5D=&q%5Bsort%5D=&q%5Byear_from%5D=&q%5Byear_to%5D='
response = requests.get(url)
soup1 = BeautifulSoup(response.content, 'html.parser')
cars = soup1.find_all('div', attrs={'class':'products-i'})

price = []
model = []
distance = []
engine = []
year = []
date_and_city = []

for car in cars:
    car_price = car.find('div', attrs={'class':'product-price'}).get_text()
    price.append(car_price)

    car_model = car.find('div', attrs={'class': 'products-i__name products-i__bottom-text'}).get_text()
    model.append(car_model)

    car_distance_covered = car.find('div', attrs={'class': 'products-i__attributes products-i__bottom-text'}).get_text()[14:]
    distance.append(car_distance_covered)

    car_engine = car.find('div', attrs={'class': 'products-i__attributes products-i__bottom-text'}).get_text()[6:11]
    engine.append(car_engine)

    car_year = car.find('div', attrs={'class': 'products-i__attributes products-i__bottom-text'}).get_text()[:4]
    year.append(car_year)

    car_city_datetime = car.find('div', attrs={'class': 'products-i__datetime'}).get_text()
    date_and_city.append(car_city_datetime)

cars_dataframe = pd.DataFrame({'Price' : price, 'Model' : model, 'Distance' : distance, 'Engine' : engine, 'Year' : year, 'Date and City' : date_and_city})

cars_dataframe.to_excel('Malibu_data5.xlsx')






