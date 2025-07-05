from collections import defaultdict
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.followers_map = defaultdict(set)
        self.tweets_map = defaultdict(set)

        self.timestamp = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets_map[userId].add((-self.timestamp, tweetId))
        self.timestamp = self.timestamp +1

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = list(self.tweets_map[userId])

        for user_id in self.followers_map[userId]:
            all_tweets.extend(list(self.tweets_map[user_id]))

        heapq.heapify(all_tweets)

        news_feed, news_count = list(), 0
        while all_tweets and news_count < 10:
            _, tweet_id = heapq.heappop(all_tweets)
            news_feed.append(tweet_id)
            news_count = news_count +1
        
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers_map[followerId]:
            self.followers_map[followerId].remove(followeeId)