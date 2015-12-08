import os
import tweepy

auth = tweepy.OAuthHandler(os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"])

api = tweepy.API(auth)
user = api.get_user("iammrinal0")
print(user.screen_name)
