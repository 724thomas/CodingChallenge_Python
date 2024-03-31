#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        cnums = []
        for n in nums:
            if len(cnums) == k:
                if n > cnums[0]:
                    heapq.heappop(cnums)
                    heapq.heappush(cnums, n)
            else:
                heapq.heappush(cnums, n)
        return cnums[0]