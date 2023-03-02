# https://leetcode.com/problems/combination-sum/

'''
1. 아이디어 :
    백트래킹, dfs로 풀 수 있다.
2. 시간복잡도 :
    O(n^2)
3. 자료구조 :
    배열
'''


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(index, total):
            if total > target:
                return
            if total == target:
                res.append(curr.copy())
                return

            for i in range(index, len(candidates)):
                curr.append(candidates[i])
                dfs(i, total+candidates[i])
                curr.pop()

        dfs(0,0)
        return res
