#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import deque
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        nnums = nums * 2
        ones = nums.count(1)
        zero_one = [0,0]
        i = 0
        for i in range(ones):
            zero_one[nums[i]] += 1
        ans = zero_one[0]
        for i in range(i+1, len(nums)+ ones):
            zero_one[nnums[i]] += 1
            zero_one[nnums[i-ones]] -= 1
            ans = min(ans, zero_one[0])
        return ans


