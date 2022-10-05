from itertools import count
from flask import *
from credentials import *
import tweepy

app = Flask(__name__)
'''
# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)'''

# Create API object
api = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAGFJhwEAAAAAtmgQqi4yRSbewBgx1Kd7%2FbfvrEM%3DNmdOePO17SLwaJpBtpdYJUVh9rOUOjUhwy5NNJJjm4XcRbcu6T')

def getHashStats(tag):
    countData = api.get_recent_tweets_count(tag, granularity='day')
    dayCount = countData.data[-1]['tweet_count']
    weekCount = countData.meta['total_tweet_count']
    return {'dayCount':str(dayCount), 'weekCount':str(weekCount)}

@app.route('/')
def index():
    countData = getHashStats('lol')
    return("Day count: " + countData['dayCount'] + "</br> Week Count: " + countData['weekCount'])
    