#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        def val(x,y):
            cur=grid[x][y]
            row=max(grid[x])
            col=0
            for r in range(len(grid)):
                col=max(col, grid[r][y])
            grid[x][y]=(max(grid[x][y],min(row,col)))
            return grid[x][y]-cur

        row=col=len(grid)
        ans=0
        for r in range(row):
            for c in range(col):
                ans+= val(r,c)
        return ans