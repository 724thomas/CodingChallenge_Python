# https://www.acmicpc.net/problem/2667

'''
1. 아이디어 :
    dfs로 풀 수 있다
2. 시간복잡도 :
    O(n^2)
3. 자료구조 :
    배열
'''
import sys

input = sys.stdin.readline
graph = [list(map(int, input().rstrip())) for _ in range(int(input()))]
ans = []
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(row, col):
    if row < 0 or row >= len(graph) or col < 0 or col >= len(graph[0]) or graph[row][col] == 0:
        return 0

    graph[row][col] = 0
    counts = 0
    for row2, col2 in dir:
        counts += dfs(row + row2, col + col2)

    return counts+1

for row in range(len(graph)):
    for col in range(len(graph[0])):
        if graph[row][col] == 1:
            ans.append(dfs(row, col))

ans.sort()
print(len(ans))
for i in ans:
    print(i)
