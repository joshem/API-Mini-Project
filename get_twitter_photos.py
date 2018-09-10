from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
import wget
import passwords


    auth = OAuthHandler(passwords.CONSUMER_KEY, passwords.CONSUMER_SECRET)
    auth.set_access_token(passwords.ACCESS_TOKEN, passwords.ACCESS_TOKEN_SECRET)
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
    x = 1
    for image in images:
    	image_path = "/home/joshuastern/Documents/601/API_Mini_Project/images/twitterimage"
    	y = str(x)
    	z = ".jpg"
    	new_image_path = image_path + y + z
    	wget.download(image, new_image_path)
    	x = x+1
