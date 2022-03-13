import os
import tweepy
import time
from dotenv import load_dotenv
load_dotenv()

consumer_key = os.environ.get("API_KEY")
consumer_secret = os.environ.get("API_KEY_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

query = 'cc @sseraphini'

replied_tweets = []
while (True):
   time.sleep(10)
   tweet_to_reply = api.search_tweets(q=query)[0]._json['id']

   if (tweet_to_reply not in replied_tweets):
      api.update_status(status='depende', in_reply_to_status_id=tweet_to_reply, auto_populate_reply_metadata=True)
      replied_tweets.append(tweet_to_reply)
      print(replied_tweets)
