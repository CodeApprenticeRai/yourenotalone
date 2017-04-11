from flask import render_template
from app import app
#from reddit_handler import *
import praw
import random

#Reddit Authentication
reddit = praw.Reddit(client_id = 'BtMcH7T6b8lFVg', client_secret = 'g09qUNlgWGY48KCWy7iCvK6Bah4', user_agent ='web:yourenotalone_us:v0.0.1 (by /u/yourenotalone_us')
subreddit = reddit.subreddit('depression')
dpostdic = {}

#gets title, post pairs
def get_pairs():
    for submission in subreddit.hot(limit=50):
        if 100 > submission.score:
            dpostdic[str(submission.title)] = submission.selftext
    return dpostdic

def clean_pairs():
    for key, value in dpostdic.items():
        if 'reddit' in (key or value):
            del dpostdic[value]


#Copypaste from Flask Tutorial Site (Only half certain what this doesx)
@app.route('/')
@app.route('/index')


def index():
    get_pairs()
    clean_pairs()
    #choose a random title, post pair from the above dictionary
    d_title, d_post = random.choice(list(dpostdic.items()))
    d_user = "-Anonymous Writer" + " " + str(random.choice(range(0,1000)))
    return render_template('index.html', d_title = d_title.capitalize(), d_post = d_post, d_user = d_user)
