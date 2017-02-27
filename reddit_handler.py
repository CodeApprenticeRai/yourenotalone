#yourenotalone_us
#usyourenotalone
import pprint
import praw
import random

reddit = praw.Reddit(client_id = 'BtMcH7T6b8lFVg', client_secret = 'g09qUNlgWGY48KCWy7iCvK6Bah4', user_agent ='web:yourenotalone_us:v0.0.1 (by /u/yourenotalone_us')
subreddit = reddit.subreddit('depression')


dpostdic = {}
#gets title, post pairs
def get_pairs():
    for submission in subreddit.hot(limit=50):
        if 100 > submission.score:
            dpostdic[str(submission.title)] = submission.selftext
    return dpostdic

#cleans text for newlines and other things

def get_rand_pair():
    d_title, d_post = random.choice(list(dpostdic.items()))
    print d_title, d_post
    return d_title, d_post

get_pairs()
get_rand_pair()
