#!/usr/bin/env python3
import sys
import time

from shutdownstem.scraper import main


if __name__=="__main__":
    start = time.time()
    print(f"[*] starting at {start}")
    if len(sys.argv) == 2:
        hashtag = sys.argv[1]
        main(hashtag)
    else:
        main()

    end = time.time()
    elapsed = end - start
    print(f"[*] elapsed time: {elapsed}")
