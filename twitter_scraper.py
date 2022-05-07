import twint
import nest_asyncio
import pandas as pd

nest_asyncio.apply()


def tweets_scraper(search_term,
                   since,
                   search_limit=None,
                   export_data=False,
                   search_language="English",
                   export_pandas=True,
                   hide_output=True,
                   debug=False):
    """


    Parameters
    ----------
    search_term : string
        The term with which you want to query Twitter database
    since : string
        Date since which you want to query the Twitter database
        The accepted format is: "YYYY-MM-DD"
    search_limit : int, optional
        Number of results you want to return. For very famous topics
        just using since parameter might return huge data, limiting
        the search could improve response time.
        The default is None.
    export_data : boolean, optional
        Set it to True if you want to export the data, the name of
        the file will be {search_term}_{since}_twitter_data.csv".
        The default is False.
    search_language : string, optional
        The language of Tweets to be searched.
        The default is "English".
    export_pandas : boolean, optional
        Exports data as pandas dataframe. JSON format is not supported yet.
        The default is True.
    hide_output : boolean, optional
        The twint package by default shows the tweets collected in the console.
        To avoid it, hide_output is set to True.
        The default is True.
    debug : boolean, optional
        This is used to generate log files for the query. Keep this as True to
        debug the scraping process.
        The default is False.

    Returns
    -------
    data : TYPE
        DESCRIPTION.

    """

    tweets = twint.Config()

    tweets.Search = search_term
    tweets.Limit = search_limit
    tweets.Since = since
    tweets.Lang = search_language
    tweets.Pandas = export_pandas
    tweets.Hide_output = hide_output
    tweets.Debug = debug

    twint.run.Search(tweets)

    data = twint.storage.panda.Tweets_df

    if len(data) == 0:
        print(f"[-] No data found for the search term: {search_term}")
        return pd.DataFrame()

    if export_data:
        data.to_csv(f"{search_term}_{since}_twitter_data.csv")

    return data
