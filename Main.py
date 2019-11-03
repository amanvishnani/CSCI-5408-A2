from config import news_api_collection, twitter_collection, file_name
from twitter import storeTweetToMongo, cleanTweets, getAllTweets
from news_api import storeNewsToMongo, cleanNews, getAllNews

# Data Collection
storeTweetToMongo(collection=twitter_collection)
storeNewsToMongo(news_api_collection)

# Data Cleaning
# 1. Clean twitter Data
cleanTweets(twitter_collection)
# 2. Clean News Api Data
cleanNews(news_api_collection)

# Dump Clean Text
tweets = getAllTweets(twitter_collection)
news = getAllNews(news_api_collection)
all_text = tweets + news
try:
    file = open(file_name, "w+")
    for item in all_text:
        file.write(item+"\n")
    file.close()
except Exception as e:
    print(e)