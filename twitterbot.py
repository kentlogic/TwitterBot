import tweepy
import time

#Enter your API tokens
auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')

api = tweepy.API(auth)
user = api.me()

#Show current user
print(f'Authenticated as {user.name}')

#Show public tweets in user's timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
   print(tweet.text)
   print('################################################')

#Show user's followers
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    print(f'{follower.name} follows you.\n')

#Handle the twitter ratelimit
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)
        #For 3.7 or newer behavior. More on https://docs.python.org/3/whatsnew/3.7.html
    except StopIteration:
        return


#Search hashtags
tag_list = ["python3","linux"]

for tag in tag_list:
	#Set the number of tweets
	for tweet in tweepy.Cursor(api.search, tag).items(7):
	    #print(tweet)
	    try:
	    	#Like the tweet
	    	tweet.favorite()
	    	print(f'[ {tweet.text} ] by [ {tweet.author.name} ] has been liked.')
	    	print('============================================================')
	    except tweepy.TweepError as e:
	    	#Print the error (e.g tweet has already been liked.)
	    	print(e.reason)
	    except StopIteration:
	    	break
