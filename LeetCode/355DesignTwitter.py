#https://leetcode.com/problems/design-twitter/

'''
1. 아이디어 :
    1)  follow는 해시맵 안에 해시셋, tweet은 deque(양방향 큐)를 만든다.
    postTweet : 제일 최신부터 저장하기 위해 deque의 왼쪽에 추가한다.
    getNewsFeed : deque를 앞에서부터 탐색하면서, userId가 follow한 사람이거나 자기 자신이면 ans에 추가한다.
    follow : HashMap[userId]에 followeeId를 추가한다.
    unfollow : HashMap[userId]에 followeeId를 제거한다. (try로 없을 시에 예외처리)
2. 시간복잡도 :
    1)  follow는 해시맵 안에 해시셋, tweet은 deque(양방향 큐)를 만든다.
    postTweet : O(1)
        deque 추가
    getNewsFeed : O(k)
        k는 트윗의 갯수. 최대 k번 탐색
    follow : O(1) * O(1)
        해시맵 검색 * 해시셋 추가
    unfollow : O(1) * O(1)
        해시맵 검색 * 해시셋 제거
3. 자료구조 :
    1) deque, 해시맵, 해시셋
'''
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = deque()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.appendleft([userId,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        count=0
        ans=[]
        while len(ans)<10 and count<len(self.tweets):
            if self.tweets[count][0] in self.follows[userId] or self.tweets[count][0] == userId:
                ans.append(self.tweets[count][1])
            count+=1
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        try:
            self.follows[followerId].remove(followeeId)
        except:
            pass