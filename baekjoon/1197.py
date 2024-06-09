# https://www.acmicpc.net/problem/1197

'''
1. 아이디어 :
    edge를 작은것부터 정렬을 시킨다.
    0번째부터 시작하여 0이랑 연결된 정점들을 heap에 넣는다.
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    최소힙
'''

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

import heapq
def solution(n, edges):
    graph = [[] for _ in range(n)]
    for u, v, weight in edges:
        graph[u].append((weight,v))
        graph[v].append((weight,u))

    visited=set()
    min_heap = [(0,0)]
    mst_weight = 0

    while min_heap and len(visited) < n:
        weight, u = heapq.heappop(min_heap)
        if u in visited:
            continue

        visited.add(u)
        mst_weight += weight

        for edge in graph[u]:
            if edge[1] not in visited:
                heapq.heappush(min_heap, edge)

    return mst_weight




n, m = list(map(int, input().split()))
edges = []
for _ in range(n):
    u, v, weight = list(map(int, input().split()))
    edges.append([u-1, v-1, weight])
print(solution(n,edges))


