#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict, deque
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dir = [[0,1],[0,-1],[1,0],[-1,0]]

        def bfs(row, col, visited):
            queue = deque()
            queue.append((row, col))
            visited.add((row, col))

            while queue:
                x, y = queue.popleft()

                for x2, y2 in dir:
                    nx, ny = x+x2, y+y2
                    if not (0<=nx<n and 0<=ny<m) or (nx,ny) in visited or grid[nx][ny] == 0:
                        continue
                    visited.add((nx,ny))
                    queue.append((nx,ny))
            return visited

        def count_lands():
            ans = 0
            visited = set()
            for row in range(n):
                for col in range(m):
                    if grid[row][col] == 1 and (row,col) not in visited:
                        ans+=1
                        visited = bfs(row,col, visited)
            return ans

        if count_lands() != 1:
            return 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    if count_lands() != 1:
                        return 1
                    grid[row][col] = 1
        return 2

