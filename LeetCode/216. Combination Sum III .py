# https://leetcode.com/problems/combination-sum-iii/description/

'''
1. 아이디어 :
    1부터 9까지의 숫자를 백트래킹을 이용하여 더하고, n과 같고 k와 같은 경우에만 ans에 추가한다.
2. 시간복잡도 :
    O(N!)
3. 자료구조 :
    리스트
'''

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtrack(nums = [], total = 0, idx=0):
            if total > n or len(nums) > k:
                return

            if total == n and len(nums) ==k:
                ans.append(nums.copy())
                return

            for i in range(idx+1, 10):
                backtrack(nums+[i], total + i, i)


        backtrack()
        return ans