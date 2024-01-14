# https://leetcode.com/problems/number-of-islands/description/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        dir = ((0,1), (0,-1), (-1,0), (1,0))

        def dfs(row1, col1):
            grid[row1][col1] = "0"

            for row2, col2 in dir:
                nrow = row1 + row2
                ncol = col1 + col2
                if 0<=nrow<len(grid) and 0<=ncol<len(grid[0]) and grid[nrow][ncol] == "1":
                    dfs(nrow, ncol)

        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    ans+=1
                    dfs(row,col)
        return ans