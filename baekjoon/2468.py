# https://www.acmicpc.net/problem/2468

'''
1. 아이디어 :
    dfs로 풀면 시간초과
    bfs로 푼다.
2. 시간복잡도 :
    O(n^2)
3. 자료구조 :
    배열
'''
from collections import deque
import sys

input = sys.stdin.readline


n = int(input())
graph = []
maxNum = 0

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > maxNum:
            maxNum = graph[i][j]


dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(a, b, value, visited):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1

    while q:
        x, y = q.popleft()

        for row2, col2 in dir:
            nx = x + row2
            ny = y + col2
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


result = 0
for i in range(maxNum):
    visited = [[0] * n for i in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i, visited)
                cnt += 1

    if result < cnt:
        result = cnt

print(result)