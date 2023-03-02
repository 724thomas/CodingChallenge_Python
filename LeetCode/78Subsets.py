#https://leetcode.com/problems/subsets/

'''
1. 아이디어 :
    백트래킹. dfs로 풀 수 있다.
2. 시간복잡도 :
    O(n^2)
3. 자료구조 :
    배열
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i):
            if i>=len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i+1)

            curr.pop()
            dfs(i+1)

        dfs(0)
        return res
