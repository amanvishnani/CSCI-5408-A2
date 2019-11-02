from config import  news_api_collection, twitter_collection
from twitter import storeTweetToMongo
from news_api import storeNewsToMongo


input = int(
    input("""
    Please Provide input:
    1. Collect Tweets
    2. Collect News
    """))

if input == 1:
    storeTweetToMongo(collection=twitter_collection)
elif input == 2:
    storeNewsToMongo(collection=news_api_collection)
