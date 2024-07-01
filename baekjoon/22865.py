# https://www.acmicpc.net/problem/22865

'''
1. 아이디어 :
    다익스트라
2. 시간복잡도 :
    O( e log v )
3. 자료구조 :
    배열. 해시셋
'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict
import heapq


def solution(n, m, a, b, c, graph):
    def bfs(start):
        distances = [float('inf')] * (n + 1)
        distances[start] = 0
        min_heap = [(0, start)]  # total, start

        while min_heap:
            curr_dist, curr = heapq.heappop(min_heap)
            if curr_dist > distances[curr]:
                continue

            for neighbor, distance in graph[curr]:
                total = curr_dist + distance
                if total < distances[neighbor]:
                    distances[neighbor] = total
                    heapq.heappush(min_heap, (total, neighbor))
        return distances

    to_a = bfs(a)
    to_b = bfs(b)
    to_c = bfs(c)

    friends = {a, b, c}
    node = -1
    distance = -1

    for start in range(1,n+1):
        if start in friends:
            continue
        closest = min(to_a[start], to_b[start], to_c[start])
        if closest > distance:
            node = start
            distance = closest
    return node

n = int(input())
a, b, c = list(map(int, input().strip().split()))
m = int(input())
graph = defaultdict(list)
for _ in range(m):
    u, v, d = list(map(int, input().strip().split()))
    graph[u].append((v, d))
    graph[v].append((u, d))

print(solution(n, m, a, b, c, graph))
