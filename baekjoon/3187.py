# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()


def solution(r, c, arr):
    ans = [0, 0]
    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def dfs(row, col):
        if arr[row][col] == "v":
            ws[1] += 1
        elif arr[row][col] == "k":
            ws[0] += 1
        arr[row][col] = "#"
        for row2, col2 in dir:
            nr, nc = row + row2, col + col2
            if not (0 <= nr < r and 0 <= nc < c) or arr[nr][nc] == "#":
                continue
            dfs(nr, nc)

    for row in range(r):
        for col in range(c):
            if arr[row][col] != "#":
                ws = [0, 0]
                dfs(row, col)
                if ws[0] > ws[1]:
                    ans[0] += ws[0]
                else:
                    ans[1] += ws[1]

    return ans


if __name__ == '__main__':
    r, c = list(map(int, input().strip().split()))
    arr = list(list(map(str, input().strip())) for _ in range(r))
    print(*solution(r, c, arr))
