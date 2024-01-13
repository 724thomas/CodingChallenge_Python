# https://leetcode.com/problems/interleaving-string/description/

'''
1. 아이디어 :
    dfs로 풀면 시간초과
    memoization을 사용
2. 시간복잡도 :
    O( n^2 )
3. 자료구조 :

'''

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo={}

        def dfs(s1_idx, s2_idx, s3_idx):
            if s3_idx == len(s3):
                return True

            if (s1_idx, s2_idx) in memo:
                return memo[(s1_idx, s2_idx)]

            ans = False
            if s1_idx < len(s1) and s1[s1_idx] == s3[s3_idx]:
                ans = ans or dfs(s1_idx+1, s2_idx, s3_idx+1)

            if s2_idx < len(s2) and s2[s2_idx] == s3[s3_idx]:
                ans = ans or dfs(s1_idx, s2_idx+1, s3_idx+1)

            memo[(s1_idx, s2_idx)] = ans
            return ans

        return dfs(0, 0, 0)