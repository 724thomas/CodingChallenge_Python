# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

'''
1. 아이디어 :
    dfs와 dp를 이용한다.
    1) dfs로 각 칸에서 가장 긴 경로를 구한다.
    2) dp로 각 칸에서 가장 긴 경로를 저장한다.
    3) dfs로 각 칸에서 가장 긴 경로를 구할 때, 이미 구한 경로는 dp에서 가져온다.
    4) dfs로 각 칸에서 가장 긴 경로를 구할 때, 이미 구한 경로는 dp에 저장한다.
2. 시간복잡도 :
    O(n^2)
3. 자료구조 :
    배열
'''

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}

        dir =[[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r, c, prevVal):
            if r<0 or r==len(matrix) or c<0 or c == len(matrix[0]) or matrix[r][c]<=prevVal:
                return 0

            if (r,c) in dp:
                return dp[(r,c)]

            res = 1
            for r2, c2 in dir:
                res = max(res, 1+dfs(r+r2, c+c2, matrix[r][c]))
            dp[(r,c)] = res
            return res

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                dfs(r,c,-1)
        return max(dp.values())