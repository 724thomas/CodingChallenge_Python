#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        prev = defaultdict(int)
        prev[0] = 1

        for i in range(len(nums)):
            curr = defaultdict(int)
            for k, v in prev.items():
                curr[k-nums[i]] += v
                curr[k+nums[i]] += v
            prev = curr
        return prev[target]