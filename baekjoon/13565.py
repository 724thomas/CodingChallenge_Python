# https://www.acmicpc.net/problem/13565

'''
1. 아이디어 :
    dfs로 풀 수 있다
2. 시간복잡도 :
    O(n * m)
3. 자료구조 :
    배열, 해시셋
'''

import sys

sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()


def solution(n, m, grid):
    visited = set()

    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def dfs(row, col):
        if row == n - 1:
            ans[0] = True
            return

        for row2, col2 in dir:
            nr, nc = row + row2, col + col2
            if not (0 <= nr < n and 0 <= nc < m) or (nr, nc) in visited or grid[nr][nc] == "1":
                continue
            visited.add((nr, nc))
            dfs(nr, nc)

    ans = [0]
    visited = set()
    for col in range(m):
        if (0,col) in visited:
            continue
        dfs(0, col)
        if ans[0]:
            return "YES"

    return "NO"


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    grid = list(list(input().strip()) for _ in range(n))  # "0 0 0 0", "0 0 0 0"
    print(solution(n, m, grid))
