#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        dir = [[0,1],[0,-1],[1,0],[-1,0]]

        def bfs(row, col):
            grid[row][col] = "0"
            queue = deque()
            queue.append((row,col))

            while queue:
                row1, col1 = queue.popleft()
                for row2, col2 in dir:
                    nrow, ncol = row1 + row2, col1 + col2
                    if not(0<=nrow<len(grid) and 0<=ncol<len(grid[0])):
                        continue
                    if grid[nrow][ncol] == "0":
                        continue
                    grid[nrow][ncol] = "0"
                    queue.append((nrow, ncol))

        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    ans += 1
                    bfs(row,col)
        return ans

