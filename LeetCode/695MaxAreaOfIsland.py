# https://leetcode.com/problems/max-area-of-island/description/

'''
1. 아이디어 :
    dfs 로 풀 수 있다.
2. 시간복잡도 :
    O(4mn)
    4 방향 탐색 * grid 크기
3. 자료구조 :

'''


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        cmax = 0

        def dfs(x,y):
            if x<0 or y<0 or x==len(grid) or y==len(grid[0]) or grid[x][y] != 1:
                return 0

            grid[x][y]=0
            return 1 + dfs(x+1,y) + dfs(x-1,y) + dfs(x,y+1) + dfs(x,y-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0:
                    cmax = max(cmax, dfs(i,j))

        return cmax