#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "776243113-z9jNEhNUMECXGSh7vHbMal10LeEkd2vGdd8Vy8F8"
access_token_secret = "6dqLRjGG8qPNW0YsEzWqINhIPq7CfzbX8y5nKyDQ6mtt1"
consumer_key = "NTVroqkzHOqyqHmDoJW2epHdy"
consumer_secret = "PoG0Bs0syXbrNgjiDldVU2gWaVD9bZSfD9SkTcO0MFJyTPrurS"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['CandyCrush', 'candycrush', 'Candy Crush', 'candy crush'])
