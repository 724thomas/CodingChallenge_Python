#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        arr = sorted([[v, k] for k, v in c.items()])

        ans = len(tasks)
        max_heap = []
        wait = deque()
        for i in range(len(arr)):
            v, k = arr[i]
            heapq.heappush(max_heap, (-v, 0))

        curr = 0
        while max_heap or wait:
            if max_heap and max_heap[0][1] <= curr:
                count, time = heapq.heappop(max_heap)
                count *= -1
                if count >= 2:
                    wait.append((count-1, curr+n))

            if wait and wait[0][1] <= curr:
                count, time = wait.popleft()
                heapq.heappush(max_heap, (-count, time))

            curr += 1
        return curr