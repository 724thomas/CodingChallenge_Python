# https://www.acmicpc.net/problem/1743

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, m, k, foods):
    def dfs(row1, col1):
        counts = 1

        grid[row1][col1] = "."
        for row2, col2 in dir:
            nrow, ncol = row1 + row2, col1 + col2
            if not (0 <= nrow < len(grid) and 0 <= ncol < len(grid[0])):
                continue
            if grid[nrow][ncol] == "#":
                counts += dfs(nrow, ncol)

        return counts

    grid = [["." for _ in range(m)] for _ in range(n)]
    for r, c in foods:
        grid[r][c] = "#"

    dir = [[1, 0], [-1, 0], [0, -1], [0, 1]]

    ans = 0
    for row in range(n):
        for col in range(m):
            if grid[row][col] == "#":
                ans = max(ans, dfs(row, col))

    return ans

n, m, k = list(map(int, input().split()))
foods = []
for _ in range(k):
    a, b = list(map(int, input().split()))
    foods.append((a - 1, b - 1))
print(solution(n, m, k, foods))
