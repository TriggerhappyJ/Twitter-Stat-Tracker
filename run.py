from flask import *
import tweepy
import datetime

app = Flask(__name__)

# Create API object
api = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAGFJhwEAAAAAtmgQqi4yRSbewBgx1Kd7%2FbfvrEM%3DNmdOePO17SLwaJpBtpdYJUVh9rOUOjUhwy5NNJJjm4XcRbcu6T')

# Search variable to use globally
searchTerm = 'example'

# Uses user query to retrieve data from api
def getSearchedStats(query):

    # Checks if search is empty, if it is set example search
    if query == '': 
        query = 'example'

    # Fixes up user search to either search a hashtag even if no # is included. 
    # Will only search username if @ is included by user
    if '@' in query:
        fixedQuery = 'from:'+query.lstrip('@')
    elif '#' in query:
        fixedQuery = query
    else:
        fixedQuery = '#'+query
        query = fixedQuery

    # Retieves data from api
    countData = api.get_recent_tweets_count(fixedQuery, granularity='day')
    dayCountData = api.get_recent_tweets_count(fixedQuery, granularity='hour')

    # Grabs specific data wanted (todays count, weekly count)
    # For day it gets the data hourly and adds together the data since midnight
    dayCountList = []
    for i in range(0, datetime.datetime.now().hour): 
       dayCountList.append(dayCountData.data[-i+1]['tweet_count'])
    dayCount = sum(dayCountList)
    weekCount = countData.meta['total_tweet_count']

    # Returns data for both main counts and graph
    return {'dayCount':dayCount, 
    'weekCount':weekCount, 
    'searchTerm':query, 
    'b1':countData.data[1]['tweet_count'],
    'b2':countData.data[2]['tweet_count'],
    'b3':countData.data[3]['tweet_count'],
    'b4':countData.data[4]['tweet_count'],
    'b5':countData.data[5]['tweet_count'],
    'b6':countData.data[6]['tweet_count'],
    'b7':dayCount, 
    }

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/search')
def sendResults():
    stats = getSearchedStats(searchTerm)
    return json.dumps(stats)

@app.route('/search', methods=['POST'])
def getResults():
    global searchTerm
    searchTerm = request.form['searchTerm']
    return 'Results gathered!'