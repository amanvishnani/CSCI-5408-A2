from config import  news_api_collection, twitter_collection
from twitter import storeTweetToMongo, cleanTweets
from news_api import storeNewsToMongo

# Data Collection
storeTweetToMongo(collection=twitter_collection)
# storeNewsToMongo(news_api_collection)

# Data Cleaning
# 1. Clean twitter Data
cleanTweets(twitter_collection);
# 2. Clean News Api Data
