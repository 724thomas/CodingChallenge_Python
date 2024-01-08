# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

'''
1. 아이디어 :
    dfs와 dp를 사용해서 시간복잡도를 줄인다.
2. 시간복잡도 :
    O(n^2)
3. 자료구조 :
    배열, 해시맵
'''

from collections import defaultdict
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = defaultdict(int)
        dir = ((0,1),(0,-1),(1,0),(-1,0))

        def dfs(row1, col1):
            max_length = 1
            curr = matrix[row1][col1]
            for row2, col2 in dir:
                nrow=row1+row2
                ncol=col1+col2
                if 0<=nrow<len(matrix) and 0<=ncol<len(matrix[0]) and matrix[nrow][ncol]>curr:
                    if (nrow,ncol) in dp:
                        max_length = max(max_length, dp[(nrow,ncol)]+1)
                    else:
                        max_length = max(max_length, dfs(nrow,ncol)+1)
            dp[(row1,col1)] = max_length
            return max_length

        ans = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans=max(ans, dfs(i,j))
        return ans