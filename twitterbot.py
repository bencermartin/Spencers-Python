import tweepy as twitter
import secrets
import datetime
import time

API_KEY = 'bnXqXT1QOzyRqmWo2IUSAxQee'
API_SECRET_KEY = 'AETqHMrJ6YNLaugx3NGNOmFnHCMaWNQ4cSaFehvYNDwq2mKYBT'
ACCESS_TOKEN = '1516506824421232642-cWMskMr9ajwRyCFEsLlnFI7AImSwJa'
SECRET_ACCESS_TOKEN = 'ujt0qMKgCIR2eHfxLtzwDoekNHeHeYHIkFZ6J0dRtfYz3'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAD2XbwEAAAAA0YCAHinvwrJni0OIJYV3K3mFq%2BM%3DdZRnElv8z1AKirhCfFbMSjbsSb0dzUlaM5RzydmLafjtq19WOq'

auth = twitter.OAuthHandler(secrets.API_KEY, secrets.API_SECRET_KEY)
auth.set_access_token(secrets.ACCESS_TOKEN, secrets.SECRET_ACCESS_TOKEN)
api = twitter.API(auth)

def bot(hashtags):
    while True:
        print(datetime.datetime.now())

        for hashtag in hashtags:
            for tweet in twitter.Cursor(api.search_tweets, q=hashtag, count=1).items(5):
                try:
                   id=dict(tweet._json)['id']
                   text =dict(tweet._json)['text']
                   api.retweet(id)
                   api.create_favorite(id)
                   print("Tweet ID:", id)
                   print("Tweet Text:", text)
                except twitter.errors.TweepyException as e:
                    print(e)
        time.sleep(10)

bot(['covidlifenepali'])












