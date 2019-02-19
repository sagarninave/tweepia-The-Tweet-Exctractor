import tweepy 
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

# consumer key, consumer secret, access token, access secret.
ckey="GT3xrIN0V85UdqPqUZ4E28egE"
csecret="oBzZvyTApKHxP0GSqo9lbRJ1K93CJRIovRN8zdBaic5oANGRvN"
atoken="740635692359950336-4rgBW9g1baTzcvX8rVzBBRbS08KIN39"
asecret="KgJ0LlsMeKvEIdJblamLN411HNGo3N3FezBHpJvgmu0Xa"

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

class listener(StreamListener):
    
    def on_data(self, data):
        tweet = data.split(',"text":"')[1].split('","source')[0]
        print(tweet + "\n")
        savefile = str(time.time()) + "::" + tweet
        save = open('twitterDB4.csv', 'a')
        save.write(savefile)
        save.write("\n\n")
        save.close()
        return (True)
    
    def mentioned_in_tweet(self):
        mystr=input("Enter Name to Find Person Mentioned In Paricular Tweets  : ")
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=[mystr])

    def timeline_tweet(self):
        api = tweepy.API(auth)
        public_tweets = api.home_timeline()
        for tweet in public_tweets:
            print(tweet.text)

obj=listener()
option = int(input('\n\t\t\tWhich Tweets Would You Like To Read  \n\t\t\t     1. My Timeline Tweets \n\t\t\t     2. Public Figure Mentioned Tweets\n\t\t\t   >>'))
if option==1:
    obj.timeline_tweet()
elif option==2:
    obj.mentioned_in_tweet()
else:
    print ("Invalid Choice")
