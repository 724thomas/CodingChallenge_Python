# https://www.acmicpc.net/problem/1162

'''
1. 아이디어 :
    다익스트라 사용
2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

import sys
import heapq

input = sys.stdin.readline


def dijkstra(n, k, graph):
    dist = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dist[1][0] = 0
    pq = [(0, 1, 0)]  # (cost, node, paved_roads)

    while pq:
        current_dist, u, paved = heapq.heappop(pq)

        if current_dist > dist[u][paved]:
            continue

        for v, weight in graph[u]:
            if current_dist + weight < dist[v][paved]:
                dist[v][paved] = current_dist + weight
                heapq.heappush(pq, (dist[v][paved], v, paved))

            if paved < k and current_dist < dist[v][paved + 1]:
                dist[v][paved + 1] = current_dist
                heapq.heappush(pq, (dist[v][paved + 1], v, paved + 1))

    return min(dist[n])


def solution(n, m, k, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    return dijkstra(n, k, graph)


n, m, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

print(solution(n, m, k, edges))
