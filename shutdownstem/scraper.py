import os
import pandas as pd
import pickle
import time
import tweepy


def get_api() -> tweepy.API:
    """
    Loads Twitter credentials from the environment and
    returns a tweepy.API instance
    """
    consumer_key = os.getenv("TWITTER_SCRAPE_CONSUMER_KEY")
    consumer_secret = os.getenv("TWITTER_SCRAPE_CONSUMER_SECRET")
    access_key = os.getenv("TWITTER_SCRAPE_ACCESS_KEY")
    access_secret = os.getenv("TWITTER_SCRAPE_ACCESS_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit = True)
    return api


def scrape_hashtag_and_save(api: tweepy.API, hashtag: str = "shutdownstem") -> None:
    """Scrapes all tweets, puts them in a pandas dataframe, and writes a subset of data to CSV,
    saving the full raw tweets for later analysis in a pickle file."""
    search_hashtag = f'#{hashtag}'

    raw_tweets = []
    authors = []
    text = []
    is_rt = []
    count = 0

    for tweet in tweepy.Cursor(api.search, q=search_hashtag, count=300).items():
        raw_tweets.append(tweet)
        authors.append(tweet.author.screen_name)
        text.append(tweet.text)

        # The way to tell if a tweet is an RT is by seeing if there is a 'retweeted_status'
        # attr on the Tweet object.
        if getattr(tweet, 'retweeted_status', None):
            tweet_is_rt = True
        else:
            tweet_is_rt = False

        is_rt.append(tweet_is_rt)
        count += 1

        if count % 100 == 0:
            print(f'[*] got {str(count)} tweets so far...')

    filename_str = time.strftime("%Y%m%d-%H%M%S")
    df = pd.DataFrame({'authors': authors, 'text': text, 'is_rt': is_rt})
    df.to_csv(f"{filename_str}.csv", index=False)
    print(f"[*] tweets saved to {filename_str}.csv")

    with open(f"{filename_str}.pkl", 'wb') as f:
        pickle.dump(raw_tweets, f)
        print(f"[*] raw tweets serialized to {filename_str}.pkl")


def main(hashtag: str = "shutdownstem"):
    print(f'[*] scraping #{hashtag}')
    api = get_api()
    scrape_hashtag_and_save(api, hashtag)
