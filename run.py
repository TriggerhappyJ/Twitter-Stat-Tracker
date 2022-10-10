from distutils.log import debug
from flask import *
import tweepy

app = Flask(__name__)

# Create API object
api = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAGFJhwEAAAAAtmgQqi4yRSbewBgx1Kd7%2FbfvrEM%3DNmdOePO17SLwaJpBtpdYJUVh9rOUOjUhwy5NNJJjm4XcRbcu6T')

searchTerm = '#example'

# Uses user query to retrieve data from api
def getSearchedStats(query):
    
    # Makes sure query will get correct results
    if '@' in query:
        fixedQuery = 'from:'+query.lstrip('@')
    elif '#' in query:
        fixedQuery = query
    else:
        fixedQuery = '#'+query
        query = fixedQuery


    # Retieves data from api
    countData = api.get_recent_tweets_count(fixedQuery, granularity='day')

    # Grabs specific data wanted (todays count, weekly count)
    dayCount = "{:,}".format(countData.data[-1]['tweet_count'])
    weekCount = "{:,}".format(countData.meta['total_tweet_count'])
    print(countData)

    return {'dayCount':str(dayCount), 
    'weekCount':str(weekCount), 
    'searchTerm':query, 
    'b1':countData.data[1]['tweet_count'],
    'b2':countData.data[2]['tweet_count'],
    'b3':countData.data[3]['tweet_count'],
    'b4':countData.data[4]['tweet_count'],
    'b5':countData.data[5]['tweet_count'],
    'b6':countData.data[6]['tweet_count'],
    'b7':countData.data[-1]['tweet_count'], 
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