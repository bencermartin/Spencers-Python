import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(from: NASA, or From YahooFinance) until: 2022-05-16 since:2021-01-01"
limit = 5000
tweets = []

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) ==limit:
        break
    else :
        tweets.append([tweet.date, tweet.user.username, tweet.content, tweet.likeCount])

df = pd.DataFrame(tweets,[ columns="Date", "UserName", "Tweet", "LikeCount"])
print(df)

df.to_csv ("NASA_Yahoo.tweet.csv")
