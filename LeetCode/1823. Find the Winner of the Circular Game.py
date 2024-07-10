#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import deque
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque([i for i in range(1,n+1)])
        while len(queue) >= 2:
            for i in range(k-1):
                queue.append(queue.popleft())
            queue.popleft()
        return queue[0]