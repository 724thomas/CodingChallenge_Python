#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import deque
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def make_grid(chars):
            arr = [[0] * 3 * len(chars) for _ in range(3)]
            for i in range(len(chars)):
                if chars[i] == "/":
                    for row in range(3):
                        for col in range(3):
                            if row + col == 2:
                                arr[row][(i*3) + col] = 1
                elif chars[i] == "\\":
                    for row in range(3):
                        for col in range(3):
                            if row == col:
                                arr[row][(i*3) + col] = 1
            return arr

        def bfs(row, col):
            queue = deque()
            queue.append((row,col))
            while queue:
                x, y = queue.popleft()
                for x2, y2 in dir:
                    nx, ny = x+x2, y+y2
                    if not (0<=nx<len(new_grid) and 0<=ny<len(new_grid[0])) or new_grid[nx][ny] == 1:
                        continue
                    new_grid[nx][ny] = 1
                    queue.append((nx, ny))


        dir = [[0,1],[0,-1],[1,0],[-1,0]]
        new_grid = []
        for g in grid:
            for row in make_grid(g):
                new_grid.append(row)

        count = 0
        for row in range(len(new_grid)):
            for col in range(len(new_grid[0])):
                if new_grid[row][col] == 0:
                    new_grid[row][col] = 1
                    count+=1
                    bfs(row, col)

        return count