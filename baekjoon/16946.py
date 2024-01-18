# https://www.acmicpc.net/problem/16946 벽 부수고 이동하기 4

'''
1. 아이디어 :
    1인부분들을 dfs로 돌면 3^n
    dfs와 dp를 사용하면 n^3. 둘다 시간초과
    반대로 0을 dp로 저장을 하고(bfs)
    1의 주변을 더한다.
2. 시간복잡도 :
    O( n^2 )
3. 자료구조 :
    해시셋, 해시맵
'''
import sys
from collections import deque

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = list(map(int, input().split()))

grid = [list(map(int, input().strip())) for _ in range(n)]


def solution(grid):
    visited = set()
    zeros = [[0] * m for _ in range(n)]
    group = 1
    info = {}
    info[0] = 0
    dir = [0, 1], [0, -1], [1, 0], [-1, 0]

    def bfs(start):
        queue = deque()
        queue.append(start)
        count = 1
        visited.add((start[0], start[1]))
        while queue:
            row1, col1 = queue.popleft()
            zeros[row1][col1] = group
            for row2, col2 in dir:
                nrow, ncol = row1 + row2, col1 + col2
                if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]) and (nrow, ncol) not in visited and grid[nrow][
                    ncol] == 0:
                    visited.add((nrow,ncol))
                    queue.append((nrow, ncol))
                    count += 1
        return count

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0 and (row, col) not in visited:
                info[group] = bfs((row, col))
                group += 1

    for row1 in range(len(grid)):
        for col1 in range(len(grid[0])):
            addList = set()
            if (row1, col1) not in visited:
                for row2, col2 in dir:
                    nrow, ncol = row1 + row2, col1 + col2
                    if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]):
                        addList.add(zeros[nrow][ncol])

            for add in addList:
                grid[row1][col1] += info[add]
                grid[row1][col1] %= 10

    for g in grid:
        print("".join(map(str, g)))


solution(grid)
