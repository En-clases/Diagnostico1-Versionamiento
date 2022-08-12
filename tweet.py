import pandas as pd
from pandas.io.json import json_normalize
import warnings
warnings.filterwarnings("ignore")

def Top10Retweet(content):
    top10 = []
    for line in content:
        if len(top10) == 0:
            top10.append(line.retweetCount)
        else:
            pos = 0
            for i in top10:
                if line.retweetCount > i:
                    top10.insert(pos, line.retweetCount)
                pos += 1
            if len(top10) > 10:
                top10.pop()
    print(f"Top 10 Retweet:", top10)

def Top10UserTweets(content):
    top10 = []
    for line in content:
        if len(top10) == 0:
            top10.append(line.user.tweetCount)
        else:
            pos = 0
            for i in top10:
                if line.user.tweetCount > i:
                    top10.insert(pos, line.user.tweetCount)
                pos += 1
            if len(top10) > 10:
                top10.pop()
    print(f"Top 10 User with most Tweets:", top10)

def Top10MoreTweets(content):
    print(content.sort_values('date',ascending = False).groupby('id').head(10))

def Top10Hashtags(content):
    hashtags = []
    for line in content:
        if "#" in line.content:
            pos = 0
            for i in line.content:
                if i == "#":
                    hashtag = line.content[i:]
                pos += 1
        dentro = False
        for y in hashtags:
            if y[0] == hashtag:
                y[1] += 1
                dentro = True
        if dentro == False:
            hashtags.append([hashtag, 1])
    hashtags.sort(sortHash, reverse=True)
    print(hashtags[:10])

def main():
    raw_tweets = pd.read_json(r"./archive/farmers-protest-tweets-2021-03-5.json", lines=True)
    funcion = int(input("Que funcion quieres ocupar?: "))
    if funcion == 1:
        Top10Retweet(raw_tweets)
    elif funcion == 2:
        Top10UserTweets(raw_tweets)
    elif funcion == 3:
        Top10MoreTweets(raw_tweets)
    elif funcion == 4:
        Top10Hashtags(raw_tweets)
        

def sortHash(list):
    return list[1]


raw_tweets = pd.read_json(r"./archive/farmers-protest-tweets-2021-03-5.json", lines=True)

main()
