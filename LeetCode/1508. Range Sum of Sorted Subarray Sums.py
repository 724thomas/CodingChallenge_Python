#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import heapq
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 1000000007
        minHeap = [(n,i) for i, n in enumerate(nums)]
        heapq.heapify(minHeap)

        ans = 0
        for i in range(right):
            num, index = heapq.heappop(minHeap)
            if i>= left-1:
                ans = (ans+num) % MOD
            if index+1 < n:
                next_pair = (num + nums[index+1], index+1)
                heapq.heappush(minHeap, next_pair)
        return ans