#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import heapq
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <=4:
            return 0
        min_four = sorted(heapq.nsmallest(4, nums))
        max_four = sorted(heapq.nlargest(4, nums))
        ans = float('inf')
        for i in range(4):
            ans = min(ans, max_four.pop() - min_four.pop())

        return ans