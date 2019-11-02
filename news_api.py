from newsapi import NewsApiClient
from config import news_api_key, keywords

newsapi = NewsApiClient(api_key=news_api_key)


def storeNewsToMongo(collection):
    for q in keywords:
        for i in range(1, 5):
            all_articles = newsapi.get_everything(q=q, sort_by='relevancy', page=i)
            j = 1
            for article in all_articles["articles"]:
                mongo_obj = collection.insert_one(article)
                print("{} -> {}.{} = {}".format(q, i, j, mongo_obj.inserted_id))
                j = j + 1