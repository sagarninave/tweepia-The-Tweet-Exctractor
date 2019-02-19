import tweepy

consumer_key="GT3xrIN0V85UdqPqUZ4E28egE"
consumer_secret="oBzZvyTApKHxP0GSqo9lbRJ1K93CJRIovRN8zdBaic5oANGRvN"
access_token="740635692359950336-4rgBW9g1baTzcvX8rVzBBRbS08KIN39"
access_token_secret="KgJ0LlsMeKvEIdJblamLN411HNGo3N3FezBHpJvgmu0Xa"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)
