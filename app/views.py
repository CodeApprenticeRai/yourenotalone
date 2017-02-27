from flask import render_template
from app import app
#from reddit_handler import *
import praw
import random

reddit = praw.Reddit(client_id = '', client_secret = '', user_agent ='')
subreddit = reddit.subreddit('depression')
dpostdic = {}

#gets title, post pairs
def get_pairs():
    for submission in subreddit.hot(limit=25):
        if 100 > submission.score:
            dpostdic[str(submission.title)] = submission.selftext
    return dpostdic

response = get_pairs()
d_title, d_post = random.choice(list(dpostdic.items()))

@app.route('/')
@app.route('/index')


def index():
    user = {'nickname': 'Miguel'} # fake user
    d_user = "Replace_DUser"
    return render_template('index.html', d_title = d_title, d_post = d_post, d_user = d_user, response = response)
