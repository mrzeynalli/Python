#TOP 100 TV Series from IMDB Website
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.imdb.com/search/title/?count=100&languages=en&num_votes=1000,&sort=num_votes,desc&title_type=tv_series'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'lxml')

series_data = soup.findAll('div', attrs= {'class': 'lister-item mode-advanced'})

print(series_data)

name = []
imdb = []
years = []
length = []
genre = []
votes = []

for series in series_data:
    series_name = series.h3.a.text
    name.append(series_name)

    imdb_score = series.find('div', attrs= {'class': 'inline-block ratings-imdb-rating'}).strong.text
    imdb.append(imdb_score)

    years_spent = series.find('span', attrs= {'class': 'lister-item-year text-muted unbold'}).text
    years.append(years_spent)

    serie_lenght = series.find('span', attrs={'class': 'runtime'})
    serie_lenght = serie_lenght.get_text(strip=True) if serie_lenght else "-"
    length.append(serie_lenght)

    serie_genre = series.find('span', attrs= {'class': 'genre'}).text
    genre.append(serie_genre)

    serie_votes = series.find('span', attrs={'name': 'nv'}).text
    votes.append(serie_votes)


series_DF = pd.DataFrame({'Name': name, 'IMDB': imdb, 'Years': years, 'Lenght': length, 'Genre': genre, 'Votes': votes})

series_DF.to_excel("TOP_100_Series.xlsx")
