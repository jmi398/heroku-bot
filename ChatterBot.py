# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "5I8PxDj4Vq9OAoSarQ5AMN6t7"
consumer_secret = "YQNOsnIB4DBUDTMyCdw52X5ZGXBbfDaSMrFssjml46dJvVhGxq"
access_token = "967430656409198592-5Nwp1puG2UEzoQfB2H9CXh9XrcCUqnx"
access_token_secret = "0yA8vgLUPyHhS1dZgQo2YAVLyUlOIio9BqudXUSOYLV21"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE
