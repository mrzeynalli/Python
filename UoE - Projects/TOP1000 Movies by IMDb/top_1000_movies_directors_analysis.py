# importing the modules
import pandas as pd
from tabulate import tabulate

data_url = r"https://raw.githubusercontent.com/mrzeynalli/Python/main/UoE%20-%20Projects/TOP1000%20Movies%20by%20IMDb" \
           r"/imdb_top_1000.csv "
# The data contains the details of the movies that are ranked in TOP1000 by IMDB

data = pd.read_csv(data_url)

# The below list includes the names of all the directors whose movies are listed in TOP1000
list_of_directors = list(data['Director'].unique())


# The below function returns the average IMDB score for the director name put in
def avg_imdb_for_director(director):
    return round(data[data['Director'].str.contains(director)]['IMDB_Rating'].mean(), 2)


directors_and_scores = {director: avg_imdb_for_director(director) for director in list_of_directors}


# The below function returns the count of movies included in TOP1000 for the director name put in
def count_movies_for_director(director):
    return data[data['Director'].str.contains(director)]['Series_Title'].count()


directors_and_movie_counts = {director: count_movies_for_director(director) for director in list_of_directors}


# The below function returns the average IMDB score for the director name included
def highest_ranked_movie(director):
    return \
        data[data['Director'] == director][['Series_Title', 'IMDB_Rating']].sort_values(by="IMDB_Rating",
                                                                                        ascending=False)[
            'Series_Title'].iloc[0]


directors_and_best_movies = {director: highest_ranked_movie(director) for director in list_of_directors}

# Creates a new dataframe objects specifically for directors
directors_data = pd.DataFrame(directors_and_scores.keys(), columns=['Director'])

# Adding average IMDb scores column
directors_data['Average movie IMDb'] = directors_and_scores.values()

# Adding movie count column
directors_data['Movie count in TOP1000'] = directors_and_movie_counts.values()

# Adding the highest ranked movie name columns
directors_data['Highest ranked movie'] = directors_and_best_movies.values()

# Sorting the dataset regarding the IMDb scores in descending order
directors_data.sort_values(by='Average movie IMDb', ascending=False)

# Reindexing the dataframe and dropping the previous indexes which automatically became a separate column
directors_data.reset_index().drop('index', axis=1)

print("TOP 10 movie directors with the highest average IMDb ratings are the below:")
print(tabulate(directors_data.head(10), headers=directors_data.columns, tablefmt='psql'))
