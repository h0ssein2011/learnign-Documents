import pandas as pd

path = '/home/hossein/Lats Win Files/Pandas-Cookbook-Second-Edition/data/movie.csv'
movie = pd.read_csv(path)

def shorten(col):
    return(
        str(col).replace('facebook_likes','fb').replace('for_reviews','')
    )

movie = movie.rename(columns=shorten)
movie.columns

