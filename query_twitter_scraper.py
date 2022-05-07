from twitter_scraper import tweets_scraper


data = tweets_scraper(search_term="Carbon capture",
                      search_limit=2000,
                      since="2015-01-01",
                      export_data=False)
