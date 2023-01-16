# https://www.acmicpc.net/problem/1012

'''
1. 아이디어 :
    1) (RecursionError) DFS를 사용하면서, 1이면 0으로 바꾸고, 0이면 False를 반환한다.
    2) BFS를 사용하면서, 1이면 0으로 바꾸고, 0이면 False를 반환한다.
2. 시간복잡도 :
    1) O(t) * (O(n^2) + O(n^2) + O(4*2)) = O(t*n^2)
    - 테스트케이스의 개수 * (배열 만들기 + 배열 순회 + dfs)
    2) O(t) * (O(n^2) + O(n^2) + O(4*2)) = O(t*n^2)
    - 테스트케이스의 개수 * (배열 만들기 + 배열 순회 + bfs)
3. 자료구조 :
    1) 배열
'''
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(x, y):
    queue = [(x, y)]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

import sys

input = sys.stdin.readline
cases = int(input())
for _ in range(cases):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] :
                bfs(i, j)
                result += 1
    print(result)




# 1)
# def dfs(x, y):
#     if x < 0 or x >= n or y < 0 or y >= m:
#         return False
#     if graph[x][y] == 1:
#         graph[x][y] = 0
#         dfs(x - 1, y)
#         dfs(x + 1, y)
#         dfs(x, y - 1)
#         dfs(x, y + 1)
#         return True
#     return False
#
#
# import sys
#
# input = sys.stdin.readline
# cases = int(input())
# for _ in range(cases):
#     m, n, k = map(int, input().split())
#     graph = [[0] * m for _ in range(n)]
#
#     for _ in range(k):
#         x, y = map(int, input().split())
#         graph[y][x] = 1
#     result = 0
#     for i in range(n):
#         for j in range(m):
#             if dfs(i, j):
#                 result += 1
#     print(result)