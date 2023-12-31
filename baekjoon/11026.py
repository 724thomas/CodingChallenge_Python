# https://www.acmicpc.net/problem/10026 적록색약

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input().rstrip())
grid = [list(input().rstrip()) for _ in range(n)]  # 2차배열
dir = [1, 0], [-1, 0], [0, 1], [0, -1]

def dfs(row1, col1, is_normal, from_color):
    if is_normal == 0:
        if from_color == "R" or from_color == "G":
            grid[row1][col1] = 'rg'
        else:
            grid[row1][col1] = 'b'
    else:
        if from_color == "rg":
            grid[row1][col1] = '0'
        else:
            grid[row1][col1] = '1'

    for row2, col2 in dir:
        nrow = row1 + row2
        ncol = col1 + col2
        if 0 <= nrow < n and 0 <= ncol < n and grid[nrow][ncol] == from_color:
            dfs(nrow, ncol, is_normal, from_color)


counts = [0, 0]
colors = [["R", "G", "B"], ["rg", "b"]]

for k in range(2):
    for color in colors[k]:
        for i in range(n):
            for j in range(n):
                if grid[i][j] == color:
                    counts[k] += 1
                    dfs(i, j, k, color)

print(*counts)
