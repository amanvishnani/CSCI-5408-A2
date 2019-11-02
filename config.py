from pymongo import MongoClient

# ###### UPDATE YOUR API AND CONFIG DETAILS BELOW #####
debug_tweepy = True
keywords = ['canada', 'halifax', 'university', '"dalhousie university"', '"canada education"']

mongo_url = 'mongodb://localhost:27017/'
mongo_db_name = 'assignment2'
mongo_twitter_collection = 'twitter_collection'
mongo_news_api_collection = 'news_api_collection'

consumer_key = 'xxx'
consumer_secret = 'xxx'
access_token = 'xxx'
access_token_secret = 'xxx'

news_api_key="xxx"

# ##########################################

client = None
db = None
twitter_collection = None
query = " OR ".join(keywords)

try:
    client = MongoClient(mongo_url)
except Exception as e:
    print(e)

if client is not None:
    db = client[mongo_db_name]
    twitter_collection = db[mongo_twitter_collection]
    news_api_collection = db[mongo_news_api_collection]
