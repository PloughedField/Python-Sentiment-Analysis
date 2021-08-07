from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob



#---------------------------------------------------------------------------

consumer_key = 'GOG1FOPMnejJGuwBnxKdaxIy9'
consumer_secret = 'rn1nCBfhbA6ESeMBqmdmU0LcktDG0WdSYMGRFueCIOwiNhMRn1'

access_token = '1066915601992560640-oOqHW7BU5piqpdeYJrwZbgRQGLRTRS'
access_token_secret = 'tsA7R0cVAkzq94TpCUbgnLRaljSS61YQIPS5cKAdRRf1z'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    # t = [[]]
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})


#---------------------------------------------------------------------------


