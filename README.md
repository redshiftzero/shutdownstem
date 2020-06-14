# shutdownstem
twitter analysis of #shutdownstem

## Setup

This code requires Python 3.7. In a virtualenv:

```
pip install -r requirements.txt
export TWITTER_SCRAPE_ACCESS_KEY=yoursecrethere
export TWITTER_SCRAPE_ACCESS_SECRET=yoursecrethere
export TWITTER_SCRAPE_CONSUMER_SECRET=yoursecrethere
export TWITTER_SCRAPE_CONSUMER_KEY=yoursecrethere
```

## Run

To scrape all tweets from the last 7 days associated with the #shutdownstem hashtag:

```
$ ./scrape.py
[*] starting at 1592161515.267193
[*] scraping #shutdownstem
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

## Further analysis

With the CSV file (not committed) one can do further analysis via:

```
>>> import pandas as pd
>>> df = pd.read_csv('20200614-135000.csv')
>>> df.head()
         authors                                               text  is_rt
0    Dudeminator  RT @BretWeinstein: I like horses but dislike T...   True
1  signed_coward  RT @yasemete: 性善説というよりは、知識のない人は簡単にデモ隊や暴徒になりますか...   True
2  signed_coward  RT @yasemete: 科学誌ネイチャーが #ブラックライブズマター への支援で #sh...   True
3     metaverity  RT @Sandra_Phoma: Cite black scientists. Invit...   True
4      kainoeske  RT @claudiascosmos: I am not an academic but I...   True
>>> len(df)
83931
```

## Scraping a different hashtag

If you'd like to scrape a different hashtag there is an optional arg for that, please provide the hashtag without the hash:

```
./scrape.py MyHashtagWithoutTheHash
```