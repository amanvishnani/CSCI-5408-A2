from config import *
import time
import tweepy

tweepy.debug(debug_tweepy)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError as e:
            print(e)
            time.sleep(15 * 60)
        except StopIteration:
            yield None
        except tweepy.TweepError as e:
            print(e)
            time.sleep(15 * 60)


def findRecentRcdInCol(collection):
    try:
        result = list(collection.find().sort([('created_at', -1)]).limit(1))
        return result[0]
    except Exception as ignored:
        return None


def storeTweetToMongo(collection):
    since_id = None
    if collection is None:
        return
    recentRcd = findRecentRcdInCol(collection)
    if recentRcd is not None:
        since_id = recentRcd["id"]

    for keyword in keywords:
        for tweet in limit_handled(tweepy.Cursor(api.search, q=keyword, tweet_mode='extended', since_id=since_id).items(600)):
            if tweet is None:
                return
            mongo_obj = collection.insert_one(tweet._json)
            print(mongo_obj.inserted_id)