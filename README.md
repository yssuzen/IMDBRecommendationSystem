Title: Movie Recommendation System

This program is a movie recommendation system that suggests movies based on the user's rating history. The program uses a dataset of movie ratings provided by users and creates a correlation matrix that suggests movies based on the ratings correlation.

To run this program, you need to have the following libraries installed:
  1. NumPy
  2. Pandas

The program reads the 'users.data' and 'movie_id_titles.csv' files, which contain the following data:

  1. users.data: user_id, item_id, rating, and timestamp
  2. movie_id_titles.csv: item_id and title

The program merges the two files to create a dataframe, which is then pivoted to create a correlation matrix based on the movie titles and user ratings. The program then suggests movies that are similar to a specific movie, such as Star Wars (1977), based on the correlation matrix.

The program also eliminates movies that have less than 100 ratings, as it considers these movies to be irrelevant to the user's preferences.

The output of the program is a list of movies that are similar to the movie of choice, along with the number of ratings for each movie.

To run the program, simply execute the Python script.
