#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, abs(nums[i] - nums[(i+1) % len(nums)]))
        return ans