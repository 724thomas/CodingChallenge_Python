# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def solution(n, m, arr):
    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def bfs(row, col):
        queue = deque()
        queue.append((row, col, 0))
        visited = [[False for _ in range(m)] for _ in range(n)]
        visited[row][col] = True
        max_dist = 0

        while queue:
            x, y, dist = queue.popleft()
            max_dist = max(max_dist, dist)

            for dx, dy in dir:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 'L':
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

        return max_dist

    ans = 0
    for row in range(n):
        for col in range(m):
            if arr[row][col] == 'L':
                ans = max(ans, bfs(row, col))

    return ans

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [list(input().strip()) for _ in range(n)]
    print(solution(n, m, arr))
