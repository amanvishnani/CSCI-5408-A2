from newsapi import NewsApiClient
from config import news_api_key, keywords
from pymongo import collection
import re

newsapi = NewsApiClient(api_key=news_api_key)


def storeNewsToMongo(mongo_collection):
    for q in keywords:
        for i in range(1, 5):
            all_articles = newsapi.get_everything(q=q, sort_by='relevancy', page=i)
            for article in all_articles["articles"]:
                existing_news = mongo_collection.find_one({'title': article['title']})
                if existing_news is not None:
                    continue
                mongo_obj = mongo_collection.insert_one(article)
                print("{} -> {}".format(q, mongo_obj.inserted_id))


def cleanNews(collection):
    print("************* Cleaning News Api Data **************")
    for news in collection.find({'cleanText': None}):
        title = news['title'] or ''
        description = news['description'] or ''
        content = news['content'] or ''
        full_text = " ".join([title, description, content]) # create full text
        full_text = re.sub(r'[^A-Za-z0-9 @]+', '', full_text)  # Special Characters
        full_text = re.sub(r"\s{2,}", ' ', full_text) # Remove Extra Spaces
        full_text = full_text.strip()
        updated_news = collection.find_one_and_update({'_id': news['_id']}, {'$set': {'cleanText': full_text}})
    print("************* [DONE] Cleaning News Data **************")


def getAllNews(collection):
    news = []
    for item in collection.find({}):
        news.append(item['cleanText']);
    return news
