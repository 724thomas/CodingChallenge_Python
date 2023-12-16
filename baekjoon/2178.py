# https://www.acmicpc.net/problem/2178

'''
1. 아이디어 :
    bfs로 풀 수 있다
2. 시간복잡도 :
    O(n^2)
3. 자료구조 :
    배열, 해시셋
'''
from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

queue = deque()
queue.append((0, 0, 0))

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = set()
visited.add((0, 0))

while queue:
    row, col, count = queue.popleft()
    if row == n - 1 and col == m - 1:
        print(count + 1)
        exit()

    for row2, col2 in dir:
        new_row = row + row2
        new_col = col + col2
        if 0 <= new_row < n and 0 <= new_col < m and graph[new_row][new_col] == 1 and (new_row, new_col) not in visited:
            visited.add((new_row, new_col))
            queue.append((new_row, new_col, count + 1))
