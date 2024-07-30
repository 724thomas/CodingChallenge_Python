# https://www.acmicpc.net/problem/17141

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
from itertools import combinations
from collections import deque


def solution(n, m, arr):
    def bfs(viruses):
        queue = deque()
        visited = [[-1] * n for _ in range(n)]
        for row, col in viruses:
            queue.append((row, col, 0))
            visited[row][col] = 0

        counter = 0
        cmax = 0
        while queue:
            counter += 1
            row1, col1, time = queue.popleft()

            for row2, col2 in dir:
                nrow, ncol = row1 + row2, col1 + col2
                if 0 <= nrow < n and 0 <= ncol < n and visited[nrow][ncol] == -1 and arr[nrow][ncol] != 1:
                    visited[nrow][ncol] = time + 1
                    queue.append((nrow, ncol, time + 1))
                    cmax = max(cmax, time + 1)

        if counter != total:
            return float('inf')
        return cmax

    dir = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    candid = []
    total = 0
    for row in range(n):
        for col in range(n):
            if arr[row][col] == 2:
                candid.append((row, col))
            if arr[row][col] != 1:
                total += 1

    ans = float('inf')
    for viruses in combinations(candid, m):
        ans = min(ans, bfs(viruses))

    return ans if ans != float('inf') else -1


if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))
    arr = [list(map(int, input().strip().split())) for _ in range(n)]
    print(solution(n, m, arr))
