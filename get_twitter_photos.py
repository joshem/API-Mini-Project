import tweepy
import wget
import passwords
import sys

def get_twitter_images(num_tweets, path):
#return the images from the tweets on my twitter profile

    images = []
    firstimage = 0
    #authenticate my twitter application with private keys
    try:
        auth = tweepy.OAuthHandler(passwords.CONSUMER_KEY, passwords.CONSUMER_SECRET)
        auth.set_access_token(passwords.ACCESS_TOKEN, passwords.ACCESS_TOKEN_SECRET)
    except:
        print("Authentication Error: Check access tokens and consumer keys")
        return
    #initialize tweepy
    my_twitter = tweepy.API(auth)

    #use Cursor for pagination
    #user_timeline returns "num_photos" amount of tweets

    try:
        for tweet in tweepy.Cursor(my_twitter.user_timeline).items(num_tweets):
            #retrives image urls from tweets and downloads them into image folder
            media = tweet.entities.get('media', [])
            if(len(media)>0):
                firstimage = 1
                images.append(media[0]['media_url'])
    except:
        print("Error getting tweets from twitter: check internet connection")
        return

    if(firstimage==0):
        print("No images found in tweets");
        return

    print(images)
    x=1000

    #build path and download with wget()
    for image in images:
        image_path = path+"/twitterimage"
        y = str(x)
        z = ".jpg"
        new_image_path = image_path + y + z
        try:
            wget.download(image, new_image_path)
            x = x+1
        except:
            print("Error downloading images: check internet connection")


if __name__ == "__main__":

    if(len(sys.argv)==3):
        try:
            num_tweets = int(sys.argv[1])
        except:
            print("error in num_tweets argument")
        project_directory = sys.argv[2]
        get_twitter_images(num_tweets, project_directory)
    else:
        print("Wrong number of arguments")
