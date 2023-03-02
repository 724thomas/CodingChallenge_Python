#https://leetcode.com/problems/subsets-ii/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''



class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []

        def dfs(i, prev):
            if i>=len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i+1,nums[i])
            curr.pop()

            while i+1<len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1, nums[i])

        dfs(0,0)
        return res