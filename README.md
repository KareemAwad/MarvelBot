# MarvelBot
##Marvel Comic Book Cover Art Bot

### General Info

The project is a bot utilizing the Twitter API and Marvel API in order to fetch Comic Books and schedule tweets containing the comic book's cover art.

The project was completed using Python and deployed and hosted on AWS Lambda.

### Documentation

Twitter API Docs: https://developer.twitter.com/en/docs/twitter-api

Marvel API Docs: https://developer.marvel.com/docs

### Description

The bot accesses the Marvel API and pulls a list of all the comic books released during the week, after choosing the comic books containing data for their cover art, the cover art is appropriately formatted and the function then selects a random comic book, tweeting its associated image when scheduled. The bot uses the Tweepy Python Library to access the Twitter API, and is scheduled to run once a day using a Coudwatch trigger.
