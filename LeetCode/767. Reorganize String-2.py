#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import heapq
from collections import defaultdict
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = defaultdict(int)
        length = len(s)
        for c in s:
            counter[c] += 1

        max_heap = []
        for k, v in counter.items():
            if v-1 > length-v:
                return ""
            heapq.heappush(max_heap, (-v, k))

        ans = ""
        wait = []
        for i in range(len(s)):
            freq, char = heapq.heappop(max_heap)
            ans += char
            freq += 1
            if wait:
                heapq.heappush(max_heap, wait.pop())
            if freq == 0:
                continue
            else:
                wait.append((freq, char))
            # print(ans)
        return ans

