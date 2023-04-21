import numpy as np
import pandas as pd

column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('users.data', sep='\t', names = column_names)

movie_titles = pd.read_csv('movie_id_titles.csv')

df = pd.merge(df, movie_titles, on='item_id')

moviemat = df.pivot_table(index='user_id', columns='title', values='rating')

# Star Wars Ratings
starwars_rating = moviemat['Star Wars (1977)']
starwars_rating

# The goal is recommending movies like Star Wars
similar_starwars = moviemat.corrwith(starwars_rating)

corr_starwars = pd.DataFrame(similar_starwars, columns=['Correlation'])
#dropping NaNs
corr_starwars.dropna(inplace=True)
corr_starwars

corr_starwars.sort_values('Correlation', ascending = False).head(10)
#As you can see, results are irrelevant with Star Wars. The reason is that the number of ratings are smaller than 100. Therefore, we are going to eliminate the movies which has no more than 100 ratings.

df.drop(['timestamp'], axis = 1)

# Find mean value for all movies
ratings = pd.DataFrame(df.groupby('title')['rating'].mean())

# Descending order
ratings.sort_values('rating', ascending=False).head()

# Find number of ratings for each movie
ratings['numRating'] = pd.DataFrame(df.groupby('title')['rating'].count())
ratings.head()

# Sort movies according to number of ratings
ratings.sort_values('numRating', ascending=False).head()

corr_starwars = corr_starwars.join(ratings['numRating'])
corr_starwars

corr_starwars[corr_starwars['numRating']>100].sort_values('Correlation', ascending=False)




