from typing import List, Dict, Set, Tuple
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.tweets: Dict[str, List[Tuple[int,int]]] = defaultdict(lambda: list())
        self.followers: Dict[str, Set[str]] = defaultdict(lambda: set())
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for tweetId in self.tweets[userId][-10:]:
                heapq.heappush(heap, tweetId)

        for followee in self.followers[userId]:
            for tweetId in self.tweets[followee][-10:]:
                heapq.heappush(heap, tweetId)

        result = []
        i = 0
        while heap and i < 10:
            result.append(heapq.heappop(heap)[1])
            i += 1

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]: 
            self.followers[followerId].remove(followeeId)

twitter = Twitter();
twitter.postTweet(1, 30)
twitter.postTweet(1, 11)
twitter.postTweet(2, 10)
print(twitter.getNewsFeed(1))
print(twitter.getNewsFeed(2))
twitter.follow(1, 2)
print(twitter.getNewsFeed(1))
print(twitter.getNewsFeed(2))
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))