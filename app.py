import os
import tweepy
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

sseraphini_id = 2313873457

tweet_to_reply = api.user_timeline(user_id=sseraphini_id)[0]._json['id']
api.update_status(status='depende', in_reply_to_status_id=tweet_to_reply, auto_populate_reply_metadata=True)


# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)