#!/usr/bin/env python3

import urllib.request, urllib.parse, urllib.error
import twurl
import json



TWITTER_URL = "http://api.twitter.com/1.1/friends/list.json"

while True:
    print("")
    acct = input("Enter Twitter Account: ")
    if (len(acct) < 1):
        break
    url = twurl.augment(TWITTER_URL,
                        {"screen_name": acct,
                         "count": "5"
                         }
                        )
    print("Retrieving", url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    
    js = json.loads(data)
    print(json.dumps(js, indent=2))
    
    headers = dict(connection.getheaders())
    print("Remaining", headers["x-rate-linmit-remaining"])  # Twitter tells you how many more API requests remaining.
    
    for u in js["users"]:
        print(u["screen_name"])
        if "status" not in u:
            print("   * No status found   ")
            continue
        s = u["status"]["text"]
        print("    ", s[:50])
        