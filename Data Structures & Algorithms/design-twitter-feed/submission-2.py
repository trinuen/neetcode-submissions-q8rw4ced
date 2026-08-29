class Twitter:

    def __init__(self):
        self.posts = defaultdict(list) #{user: [[time, post]]}
        self.follows = defaultdict(set) #{user: set(followee)}
        self.i = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.i, tweetId])
        self.i -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        heapq.heapify(max_heap)
        for p in self.posts[userId]:
            heapq.heappush(max_heap, p.copy())
        for followee in self.follows[userId]:
            for p in self.posts[followee]:
                heapq.heappush(max_heap, p.copy())
        
        posts = []
        for i in range(10):
            if not max_heap:
                break
            posts.append(heapq.heappop(max_heap)[1])
        return posts

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
