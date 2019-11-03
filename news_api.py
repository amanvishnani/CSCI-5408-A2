from newsapi import NewsApiClient
from config import news_api_key, keywords
from pymongo import collection

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