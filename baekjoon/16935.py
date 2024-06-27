# https://www.acmicpc.net/problem/16935

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, m, k, grid, cmd):
    def one():
        for row in range(len(grid) // 2):
            for col in range(len(grid[0])):
                grid[row][col], grid[-1 - row][col] = grid[-1 - row][col], grid[row][col]

    def two():
        for row in range(len(grid)):
            for col in range(len(grid[0]) // 2):
                grid[row][col], grid[row][-1 - col] = grid[row][-1 - col], grid[row][col]

    def three():
        arr = [[0] * len(grid) for _ in range(len(grid[0]))]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                arr[col][-1 - row] = grid[row][col]
        return arr

    def four():
        arr = [[0] * len(grid) for _ in range(len(grid[0]))]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                arr[-1 - col][row] = grid[row][col]
        return arr

    def five():
        row_idx = len(grid) // 2
        col_idx = len(grid[0]) // 2
        for row in range(row_idx):
            for col in range(col_idx):
                grid[row][col], grid[row][col+col_idx], grid[row+row_idx][col+col_idx], grid[row+row_idx][col] = grid[row+row_idx][col], grid[row][col], grid[row][col+col_idx], grid[row+row_idx][col+col_idx]

    def six():
        row_idx = len(grid) // 2
        col_idx = len(grid[0]) // 2
        for row in range(row_idx):
            for col in range(col_idx):
                grid[row][col], grid[row][col+col_idx], grid[row+row_idx][col+col_idx], grid[row+row_idx][col] = grid[row][col+col_idx], grid[row+row_idx][col+col_idx], grid[row+row_idx][col], grid[row][col]


    for c in cmd:
        if c == 1:
            one()
        elif c == 2:
            two()
        elif c == 3:
            grid = three()
        elif c == 4:
            grid = four()
        elif c == 5:
            five()
        else:
            six()

    for g in grid:
        print(* g)



n, m, k = list(map(int, input().split()))
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
cmd = list(map(int, input().split()))
solution(n, m, k, grid, cmd)
