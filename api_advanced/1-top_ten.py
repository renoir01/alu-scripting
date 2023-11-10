#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
Requirements:

Prototype: def top_ten(subreddit)
If not a valid subreddit, print None.
NOTE: Invalid subreddits may return a redirect to search
results. Ensure that you are not following redirects.
"""
import json
import urllib.error
import urllib.parse
import urllib.request


def top_ten(subreddit):
    """
    Write a function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit.
    Requirements:

    Prototype: def top_ten(subreddit)
    If not a valid subreddit, print None.
    NOTE: Invalid subreddits may return a redirect to search
    results. Ensure that you are not following redirects.
    """
    # get your url
    url = f"https://www.reddit.com/r/{subreddit}/top.json"
    # create query parameters for pagination and filtering
    query_parameters = {
        "t": "all",
        "count": 0,
        "limit": 10
    }
    # encode query parameters and add to url
    query_parameters = urllib.parse.urlencode(query_parameters)
    url = f"{url}?{query_parameters}"
    # make request object
    req_object = urllib.request.Request(url, method="GET")
    # add custom agent
    req_object.add_header("User-Agent", "OboloScript/1.0")
    # send the url and get response agent
    try:
        with urllib.request.urlopen(req_object) as resp_object:
            resp_json = json.load(resp_object)
    except urllib.error.HTTPError:
        print(None)
    else:
        resp_children = resp_json["data"]["children"]
        for post in resp_children:
            print(post["data"]["title"])
