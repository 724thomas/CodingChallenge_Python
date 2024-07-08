#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        for h in heights:
            print(h)
        n = len(heights)
        m = len(heights[0])
        dir = [[0,1],[0,-1],[1,0],[-1,0]]

        pac = set()
        atl = set()

        def dfs(r, c, visited, prevHeight):
            if ((r,c) in visited or not(0<=r<n and 0<=c<m) or heights[r][c] < prevHeight):
                return

            visited.add((r,c))
            for r2,c2 in dir:
                nr, nc = r+r2, c+c2
                dfs(nr, nc, visited, heights[r][c])

        for c in range(m):
            dfs(0, c, pac, heights[0][c])
            dfs(n-1, c, atl, heights[n-1][c])

        for r in range(n):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, m-1, atl, heights[r][m-1])

        ans = []
        for r in range(n):
            for c in range(m):
                if (r,c) in pac and (r,c) in atl:
                    ans.append([r,c])

        return ans


