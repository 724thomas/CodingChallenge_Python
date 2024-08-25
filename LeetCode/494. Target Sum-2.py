#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import deque, defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        prev = defaultdict(int)
        prev[0] = 1

        for i in range(n):
            curr = defaultdict(int)
            for k, v in prev.items():
                curr[k+nums[i]] += v
                curr[k-nums[i]] += v
            prev = curr
            # print(prev)
        return prev[target]