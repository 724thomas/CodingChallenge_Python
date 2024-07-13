# https://www.acmicpc.net/problem/24479

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

from collections import defaultdict
def solution(n, m, r, edges):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)


    def dfs(node):
        for child in sorted(graph[node]):
            if child in visited:
                continue
            visited[child] = len(visited) + 1
            dfs(child)

    visited = {}
    visited[r] = 1
    dfs(r)
    for i in range(1, n+1):
        if i in visited:
            print(visited[i])
        else:
            print(0)


if __name__ == '__main__':
    edges = []
    n, m, r = list(map(int, input().strip().split()))
    for _ in range(m):
        edges.append(list(map(int, input().strip().split())))
    solution(n, m, r, edges)


