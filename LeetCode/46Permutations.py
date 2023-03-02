#

'''
1. 아이디어 :
    백트래킹, dfs로 풀 수 있다
2. 시간복잡도 :
    O(n!)
3. 자료구조 :
    배열
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        print(nums[:1],nums[2:])
        res = []
        curr = []
        def dfs(length, leftover):
            if length>=len(nums):
                res.append(curr.copy())
                return

            for i in range(len(leftover)):
                curr.append(leftover[i])
                dfs(length+1, leftover[:i] + leftover[i+1:])
                curr.pop()

        dfs(0, nums)
        return res