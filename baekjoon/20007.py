# https://www.acmicpc.net/problem/20007

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline

import heapq
from collections import defaultdict


def solution(n, m, x, y, edges):
    def dij(start, n, graph):
        dist = [float('inf')] * n
        dist[start] = 0
        pq = [(0, start)]

        while pq:
            curr_dist, u = heapq.heappop(pq)

            if curr_dist > dist[u]:
                continue

            for v, d in graph[u]:
                total_distance = curr_dist + d
                if total_distance < dist[v]:
                    dist[v] = total_distance
                    heapq.heappush(pq, (total_distance, v))
        return dist

    graph = defaultdict(list)
    for u, v, d in edges:
        graph[u].append((v, d))
        graph[v].append((u, d))

    dist = dij(y, n, graph)
    if max(dist) * 2 > x:
        return -1

    dist.sort()
    days = 0
    curr = 0
    for d in dist:
        if curr + 2*d > x:
            days += 1
            curr = 0
        curr += 2 * d
    if curr:
        days += 1
    return days

n, m, x, y = list(map(int, input().strip().split()))
edges = []
for _ in range(m):
    edges.append(list(map(int, input().strip().split())))
print(solution(n, m, x, y, edges))
