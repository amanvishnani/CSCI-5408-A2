from config import *
import time
import tweepy
import re

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
        print(keyword)
        for tweet in limit_handled(tweepy.Cursor(api.search, q=keyword, tweet_mode='extended', since_id=since_id).items(600)):
            if tweet is None:
                break
            mongo_obj = collection.insert_one(tweet._json)
            print(mongo_obj.inserted_id)


def cleanTweets(collection):
    print("************* Cleaning Twitter Data **************")
    for tweet in collection.find({'cleanText': None}):
        full_text = tweet['full_text']
        full_text = re.sub(url_regex, '', full_text) # Remove URL
        full_text = re.sub(r'[^A-Za-z0-9 @]+', ' ', full_text)  # Special Characters
        full_text = re.sub(r"\s{2,}", ' ', full_text) # Remove Extra Spaces
        full_text = full_text.strip()
        updated_tweet = collection.find_one_and_update({'_id': tweet['_id']}, {'$set': {'cleanText': full_text}})
    print("************* [DONE] Cleaning Twitter Data **************")


def getAllTweets(collection):
    tweets = []
    for tweet in collection.find({}):
        tweets.append(tweet['cleanText'])
    return tweets