#import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys
#Variables that constains the users credentials to access Twitter API

access_token = "3301043579-Zvgr2QC8gTUdN7Lx4XvTNuISYKLtGVfVRrDPbkX"
access_token_secret = "sjc4hH9Gk443xm65UNiwW9214HTRjCJrtMkZH6J5j8nav"
consumer_key = "VgH2w07oD7FbobkyWy0amUcpi"
consumer_secret = "BqzJNDQSSZwfZgbcxddafVgeL56xwaobuSN3XWfLg4qHR5pnB3"

##This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self,data):
        print data
        return True

    def on_error(self,status):
        print status

if __name__ == '__main__':

    argument = sys.argv[1]

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=[argument])
