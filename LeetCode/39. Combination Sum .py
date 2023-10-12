# https://leetcode.com/problems/combination-sum/description/

'''
1. 아이디어 :
    백트래킹으로 풀 수 있다.
2. 시간복잡도 :
    O(2^n)
3. 자료구조 :
    배열
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        arr = []

        def backtrack(total, idx):
            if total > target:
                return
            if total == target:
                ans.append(arr.copy())
                return

            for i in range(idx, len(candidates)):
                arr.append(candidates[i])
                backtrack(total+candidates[i], i)
                arr.pop()


        backtrack(0, 0)
        return ans