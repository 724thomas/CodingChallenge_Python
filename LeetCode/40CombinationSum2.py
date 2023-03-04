#https://leetcode.com/problems/combination-sum-ii/description/

'''
1. 아이디어 :
    모든 경우의 수를 구해야한다. 백트래킹을 사용
2. 시간복잡도 :
    O(2^n)
    해당 숫자를 포함할지, 안할지를 선택
3. 자료구조 :
    배열
'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        temp = []
        candidates.sort()
        def backtracking(pos, cnt):
            if cnt>target:
                return
            if cnt==target:
                ans.append(temp.copy())
                return

            prev=-1
            for i in range(pos, len(candidates)):
                if candidates[i]==prev:
                    continue
                temp.append(candidates[i])
                backtracking(i+1, cnt+candidates[i])
                temp.pop()
                prev = candidates[i]


        backtracking(0,0)
        return ans