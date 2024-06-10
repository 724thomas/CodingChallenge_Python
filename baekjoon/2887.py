# https://www.acmicpc.net/problem/2887

'''
1. 아이디어 :
    edges를 구할때 모든 간선들을 구하는건 n**2이므로, x,y,z별로 정렬을 한 후에 cost를 저장한다. (3*nlogn)
    스림 알고리즘을 통해서 푼다.
2. 시간복잡도 :
    O( nlogn + n*nlogn )
3. 자료구조 :
    배열, 힙
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

import heapq
def solution(n, planets):
    edges = []
    for axis in range(3):
        planets.sort(key=lambda x: x[axis])
        for i in range(1, n):
            u, v = planets[i-1][3], planets[i][3]
            cost = abs( planets[i][axis] - planets[i-1][axis])
            edges.append((cost, u, v))

    graph = [[] for _ in range(n)]
    for cost, u, v in edges:
        graph[u].append((cost, v))
        graph[v].append((cost, u))

    min_heap = [(0, 0)]  # (cost, start_node)
    visited = [False] * n
    total_cost = 0
    edges_used = 0

    while min_heap and edges_used < n:
        cost, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost
        edges_used += 1
        for next_cost, v in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (next_cost, v))

    return total_cost

n = int(input())
planets = []
for i in range(n):
    x,y,z =  list(map(int, input().split()))
    planets.append((x,y,z,i))

print(solution(n, planets))


