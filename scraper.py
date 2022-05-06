import twint
import nest_asyncio
import pandas as pd

nest_asyncio.apply()

def tweet_scraper(keyword, search_limit=1000):

    tweets = twint.Config()
    tweets.Search = keyword
    tweets.Pandas = True
    tweets.Limit = search_limit
    twint.run.Search(tweets)
    df = twint.storage.panda.Tweets_df
    return df

carbon_data = tweet_scraper("Carbon capture")