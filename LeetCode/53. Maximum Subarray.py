#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        cmax = -float('inf')
        for n in nums:
            curr += n
            cmax = max(cmax, curr)
            curr = max(curr,0)
        return cmax