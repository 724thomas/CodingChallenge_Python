# https://www.acmicpc.net/problem/21938

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

from collections import deque


def solution(n, m, arr, bound):
    narr = []
    for i in range(n):
        col = [0 if ((arr[i][j] + arr[i][j + 1] + arr[i][j + 2]) // 3) < bound else 255 for j in range(0, m * 3, 3)]
        narr.append(col.copy())
    print(*narr, sep="\n")

    count = 0
    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def bfs(r, c):
        queue = deque()
        queue.append((r, c))
        narr[r][c] = 0

        while queue:
            row, col = queue.popleft()
            for row2, col2 in dir:
                nrow, ncol = row + row2, col + col2
                if not (0 <= nrow < n and 0 <= ncol < m) or narr[nrow][ncol] == 0:
                    continue
                narr[nrow][ncol] = 0
                queue.append((nrow, ncol))

    for row in range(n):
        for col in range(m):
            if narr[row][col] == 255:
                count += 1
                bfs(row, col)
    return count


if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))
    arr = [list(map(int, input().strip().split())) for _ in range(n)]
    bound = int(input())
    print(solution(n, m, arr, bound))
