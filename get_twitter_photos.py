import tweepy
import wget
import passwords

def get_tweets(num_photos):
#return the tweets from my twitter profile

    #authenticate my twitter application with private keys
    #initialize tweepy
    auth = tweepy.OAuthHandler(passwords.CONSUMER_KEY, passwords.CONSUMER_SECRET)
    auth.set_access_token(passwords.ACCESS_TOKEN, passwords.ACCESS_TOKEN_SECRET)
    my_twitter = tweepy.API(auth)

    #use Cursor for pagination
    #user_timeline returns "num_photos" amount of tweets
    tweets = []
    for tweet in tweepy.Cursor(my_twitter.user_timeline).items(num_photos):
    	tweets.append(tweet)

    return tweets

def get_images(tweets):
    #retrives image urls from tweets and downloads them into image folder

	images = []
    #look for media urls
	for tweet in tweets:
		media = tweet.entities.get('media', [])
		if(len(media)>0):
			images.append(media[0]['media_url'])
	print(images)
	x = 1000

    #build path and download with wget()
	for image in images:
		image_path = "/home/joshuastern/Documents/601/API-Mini-Project/twitterimage"
		y = str(x)
		z = ".jpg"
		new_image_path = image_path + y + z
		wget.download(image, new_image_path)
		x = x+1


if __name__ == "__main__":

	try:
    		num_photos = 10
    		tweets = get_tweets(num_photos)
    		get_images(tweets)
	except:
		print("Unable to get photos from twitter")
