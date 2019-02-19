import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
import datetime, time

ckey="GT3xrIN0V85UdqPqUZ4E28egE"
csecret="oBzZvyTApKHxP0GSqo9lbRJ1K93CJRIovRN8zdBaic5oANGRvN"
atoken="740635692359950336-4rgBW9g1baTzcvX8rVzBBRbS08KIN39"
asecret="KgJ0LlsMeKvEIdJblamLN411HNGo3N3FezBHpJvgmu0Xa"

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

def get_tweets(api,username):
    page =1
    deadend = False
    while True:
        tweets = api.user_timeline(username, page = page)

        for tweet in tweets:
            if (datetime.datetime.now() - tweet.created_at).days<2:
                print(tweet.text.encode("utf-8"))
            else:
                deadend = True
                return
        if not deadend:
            page+1
            time.sleep(500)
            
get_tweets(api,"narendramodi")
