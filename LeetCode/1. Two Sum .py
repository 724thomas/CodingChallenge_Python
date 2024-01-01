# https://leetcode.com/problems/two-sum/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(n)
3. 자료구조 :

'''

from collections import defaultdict
class Solution(object):
    def twoSum(self, nums, target):
        visited = defaultdict(int)

        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in visited:
                return [i, visited[remain]]
            else:
                visited[nums[i]] = i

