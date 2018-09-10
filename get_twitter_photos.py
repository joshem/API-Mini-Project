from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
import wget
import twitter_credentials


    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
    my_twitter = API(auth)

    tweets = []
    for tweet in Cursor(my_twitter.user_timeline).items(1):
    	tweets.append(tweet)

	print(tweets)
	images = []
	for tweet in tweets:
		media = tweet.entities.get('media', [])
		if(len(media)>0):
			images.append(media[0]['media_url'])
	print(images)
	for image in images:
		wget.download(image, '/home/joshuastern/Documents/601/TwitterProject/myfirstimage.jpg')


