#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        cmin = cmax = 1
        for num in nums:
            cmax, cmin = max(num * cmin, num * cmax, num), min(num * cmin, num * cmax, num)
            ans = max(ans, cmax)
        return ans