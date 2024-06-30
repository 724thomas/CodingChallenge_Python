#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = []

        def backtrack(total, idx):
            if total > target:
                return
            if total == target:
                ans.append(curr.copy())
                return

            for i in range(idx, len(candidates)):
                curr.append(candidates[i])
                backtrack(total+candidates[i], i)
                curr.pop()

        backtrack(0, 0)
        return ans
