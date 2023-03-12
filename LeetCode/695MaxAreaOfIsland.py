#https://leetcode.com/problems/max-area-of-island/description/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(4mn)
3. 자료구조 :

'''


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(x,y):
            if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) or grid[x][y]!=1:
                return 0

            grid[x][y] = 0
            return 1 + dfs(x+1,y) + dfs(x-1,y) + dfs(x,y+1) + dfs(x,y-1)

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans = max(ans,dfs(i,j))
        return ans