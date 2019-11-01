import time

import tweepy

# ###### UPDATE YOUR API DETAILS BELOW #####
consumer_key = 'XXXXX'
consumer_secret = 'XXXXX'
access_token = 'XXXXX'
access_token_secret = 'XXXXX'
# ##########################################

keywords = ["canada", "halifax"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)
        except StopIteration:
            yield None


query = " ".join(keywords)

for tweet in limit_handled(tweepy.Cursor(api.search, q=query).items(100)):
    if tweet is not None:
        pass
