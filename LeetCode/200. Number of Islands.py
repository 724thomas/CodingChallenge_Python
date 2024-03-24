#

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
            if row1<0 or row1 >=len(grid) or col1<0 or col1 >=len(grid[0]) or grid[row1][col1] == "0":
                return

            grid[row1][col1] = "0"
            for row2, col2 in dir:
                nrow = row1+row2
                ncol = col1+col2
                dfs(nrow, ncol)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count+=1
                    dfs(i,j)

        return count