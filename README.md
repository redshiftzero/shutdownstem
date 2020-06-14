# shutdownstem
twitter analysis of #shutdownstem

## Setup

```
pip install -r requirements.txt
export TWITTER_SCRAPE_ACCESS_KEY=yoursecrethere
export TWITTER_SCRAPE_ACCESS_SECRET=yoursecrethere
export TWITTER_SCRAPE_CONSUMER_SECRET=yoursecrethere
export TWITTER_SCRAPE_CONSUMER_KEY=yoursecrethere
```

## Run

To scrape all tweets associated with the #shutdownstem hashtag:

```
$ python scrape.py
[*] got 100 tweets so far...
[*] got 200 tweets so far...
[*] got 300 tweets so far...
[*] got 400 tweets so far...
...
[*] got 83900 tweets so far...
[*] tweets saved to 20200614-135000.csv
[*] raw tweets serialized to 20200614-135000.pkl
```

The CSV and pickle files will contain the scraped tweets.