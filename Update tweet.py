from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

# Consumer keys and access tokens, used for OAuth
consumer_key = '7EyzTcAkINVS3T2pb165'
consumer_secret = 'a44R7WvbMW7L8I656Y4l'
access_token = 'z00Xy9AkHwp8vSTJ04L0'
access_token_secret = 'A1cK98w2NXXaCWMqMW6p'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
 
# Sample method, used to update a status
api.update_status('Hello Python Central!')
