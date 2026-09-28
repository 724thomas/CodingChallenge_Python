# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 / 알고리즘 :

'''

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def bfs(grid, n, shark_r, shark_c, shark_size):
    visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append((shark_r, shark_c, 0))
    visited[shark_r][shark_c] = True

    candidates = []

    while q:
        r, c, dist = q.popleft()

        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if visited[nr][nc]:
                continue
            if grid[nr][nc] > shark_size:
                continue

            visited[nr][nc] = True
            q.append((nr, nc, dist + 1))

            if 0 < grid[nr][nc] < shark_size:
                candidates.append((dist + 1, nr, nc))

    if not candidates:
        return None

    candidates.sort()
    return candidates[0]


def solution():
    n = int(input())
    grid = []
    shark_r, shark_c = 0, 0

    for r in range(n):
        row = list(map(int, input().split()))
        for c in range(n):
            if row[c] == 9:
                shark_r, shark_c = r, c
                row[c] = 0
        grid.append(row)

    shark_size = 2
    eaten = 0
    total_time = 0

    while True:
        target = bfs(grid, n, shark_r, shark_c, shark_size)

        if target is None:
            break

        dist, fish_r, fish_c = target

        total_time += dist
        shark_r, shark_c = fish_r, fish_c
        grid[fish_r][fish_c] = 0
        eaten += 1

        if eaten == shark_size:
            shark_size += 1
            eaten = 0

    return total_time



if __name__ == '__main__':
    print(solution())

# n = int(input().rstrip())
#
# n, m = map(int, input().split())
# n, m = list(map(int, input().split()))
# a = [c for c in input().strip()]
#
# s = input().rstrip()

# arr = list(map(int, input().strip().split()))
# arr = tuple(map(int, input().split()))
# integer_list = [int(num) for num in input().split()]
# dp = [[0 for _ in range(n)] for _ in range(n)]
# dp = [[0 for j in range(n)] for i in range(n)]
# grid = [list(input().rstrip()) for _ in range(n)] # "aaa" "bbb"
# grid = list(list(map(int, input().split())) for _ in range(n)) # "0 0 0 0", "0 0 0 0"