import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "covid"
tweets = []
limit = 450

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    print(vars(tweet))
    if len(tweets) == limit: break
    else:

        tweets.append([tweet.date, tweet.content])

        df = pd.DataFrame(tweets, columns=["Date", "Content"])

df.to_csv ("martin.csv")