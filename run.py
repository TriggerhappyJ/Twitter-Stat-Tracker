from flask import *
import tweepy

app = Flask(__name__)

# Create API object
api = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAGFJhwEAAAAAtmgQqi4yRSbewBgx1Kd7%2FbfvrEM%3DNmdOePO17SLwaJpBtpdYJUVh9rOUOjUhwy5NNJJjm4XcRbcu6T')


# Uses user query to retrieve data from api
def getSearchedStats(query):
    # Retieves data from api
    countData = api.get_recent_tweets_count(query, granularity='day')

    # Grabs specific data wanted (todays count, weekly count)
    dayCount = countData.data[-1]['tweet_count']
    weekCount = countData.meta['total_tweet_count']

    return {'dayCount':str(dayCount), 'weekCount':str(weekCount)}

@app.route('/')
def index():
    countData = getSearchedStats('#lol')
    return("Day count: " + countData['dayCount'] + "</br> Week Count: " + countData['weekCount'])
    