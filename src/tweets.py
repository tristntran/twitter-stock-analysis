import GetOldTweets3 as got


def get_tweets(query: str, start_date, end_date, max_tweets=100):
    """Gets tweets within the date range for the given query

    Args:
        query (_type_): String query for the tweets
        start_date (_type_): Start date YYYY-MM-DD
        end_date (_type_): End date YYYY-MM-DD
        max_tweets (int, optional): Maximum number of tweets fetched. Defaults to 100.

    Returns:
        _type_: _description_
    """
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query)\
                                             .setSince(start_date)\
                                             .setUntil(end_date)\
                                             .setMaxTweets(max_tweets)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    return tweets

if __name__ == "__main__":
    tweets = get_tweets("apple", "2019-04-15", "2024-04-15")
    # Print the tweets
    for tweet in tweets:
        print(tweet.text)