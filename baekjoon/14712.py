# https://www.acmicpc.net/problem/14712

'''
1. 아이디어 :
    백트래킹
2. 시간복잡도 :
    O( 2^(n*m) )
3. 자료구조 :
    배열
'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = list(map(int, input().split()))

def backtrack(row, col):
    if row == n:
        ans[0] += 1
        return

    ncol = (col + 1) % m
    nrow = row + (col + 1) // m

    backtrack(nrow, ncol)
    if grid[row - 1][col - 1] == 0 or grid[row][col - 1] == 0 or grid[row - 1][col] == 0:
        grid[row][col] = 1
        backtrack(nrow, ncol)
        grid[row][col] = 0

ans = [0]
grid = [[0] * (m+1) for _ in range(n)]
backtrack(0, 0)
print(ans[0])