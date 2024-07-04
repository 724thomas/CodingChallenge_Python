# https://www.acmicpc.net/problem/4396

'''
1. 아이디어 :
    mines와 grid 비교하면서 순회
    flag를 두고 마인을 밟으면, 연산이 끝나고 *처리
2. 시간복잡도 :
    O( n*m )
3. 자료구조 :
    배열
'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, mines, grid):
    dir = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1]
    ]

    def get_mines(r1, c1):
        mine = 0
        for r2, c2 in dir:
            nr, nc = r1 + r2, c1 + c2
            if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                continue
            if mines[nr][nc] == "*":
                mine += 1
        return str(mine)

    lost = False
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "x" and mines[row][col] == "*":
                grid[row][col] = "*"
                lost = True
            elif grid[row][col] == "x":
                grid[row][col] = get_mines(row, col)

    if lost:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if mines[row][col] == "*":
                    grid[row][col] = "*"

    for g in grid:
        print("".join(g))


n = int(input())
mine = []
for _ in range(n):
    mine.append(list(map(str, input().strip())))
grid = []
for _ in range(n):
    grid.append(list(map(str, input().strip())))
solution(n, mine, grid)
