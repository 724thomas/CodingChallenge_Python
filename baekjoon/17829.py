# https://www.acmicpc.net/problem/17829

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, grid):
    def dfs(x, y, k):
        if k == 2:
            a = grid[x][y]
            b = grid[x + 1][y]
            c = grid[x][y + 1]
            d = grid[x + 1][y + 1]
            arr = sorted([a,b,c,d])
            return arr[-2]

        else:
            k = k // 2
            a = dfs(x, y, k)
            b = dfs(x + k, y, k)
            c = dfs(x, y + k, k)
            d = dfs(x + k, y + k, k)
            arr = sorted([a,b,c,d])
            return arr[-2]

    return dfs(0, 0, n)


n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
print(solution(n, grid))
