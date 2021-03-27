import tweepy
import time
import random
from pprint import pprint
import marvelous
import requests
import os

auth = tweepy.OAuthHandler(os.environ['TWITTER_CONSUMER_KEY'],os.environ['TWITTER_CONSUMER_SECRET'])
auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'],os.environ['TWITTER_ACCESS_SECRET'])

api = tweepy.API(auth)
m = marvelous.api(os.environ['MARVEL_PUBLIC_KEY'], os.environ['MARVEL_PRIVATE_KEY'])

def tweet_image(url, message):
    filename = '/tmp/temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")


def handler(event, context):

    pulls = sorted(m.comics({
        'noVariants': True,
        'limit': 100}),
        key=lambda comic: comic.title)

    comic_dict = {}
    for comic in pulls:
        # Write a line to the file with the name of the issue, and the
        # id of the series
        thumbnail=comic.thumbnail
        path = thumbnail['path']
        if 'image_not_available' in path:
            continue
        extension = '.'+thumbnail['extension']
        img_size = '/detail'

        full_path = path+img_size+extension
        
        comic_dict[comic.title] = full_path

    comic_title = random.choice(list(comic_dict.keys()))
    comic_img = comic_dict[comic_title]

    tweet_image(comic_img, comic_title)