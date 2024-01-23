# https://leetcode.com/problems/subsets/description/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(temp, idx):
            ans.append(temp.copy())
            for i in range(idx, len(nums)):
                temp.append(nums[i])
                dfs(temp, i+1)
                temp.pop()

        dfs([],0)
        return ans