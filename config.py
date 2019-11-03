from pymongo import MongoClient

# ###### UPDATE YOUR API AND CONFIG DETAILS BELOW #####
debug_tweepy = True
keywords = ['canada', 'halifax', 'university', '"dalhousie university"', '"canada education"']
url_regex = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]+\.[a-zA-Z0-9()]+\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'
file_name = "output.txt"

mongo_url = 'mongodb://localhost:27017/'
mongo_db_name = 'assignment2'
mongo_twitter_collection = 'twitter_collection'
mongo_news_api_collection = 'news_api_collection'

consumer_key = 'iPsQb6EL9hSgFtPMplKo4GF5I'
consumer_secret = 'ivk3BAAttMufD3LjNCXdZgK7SYtAG9wKXcswm0Sw6v6e1aIN0h'
access_token = '232136758-uXFtOA52lkZ5tw2wCg2f349wOPw4OQPnnKe2ABUr'
access_token_secret = 'NiRXcIxYvKnhDFSYeXeAkW6BVRmOKITmPYHMln9iGXeYz'

news_api_key="9a32723dc1694eacb4a47b9f5298e3b1"

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
