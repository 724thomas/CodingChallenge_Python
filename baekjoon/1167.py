# https://www.acmicpc.net/problem/1167

'''
1. 아이디어 :
    bfs로 풀 수 있다.
2. 시간복잡도 :
    O(V+E)
3. 자료구조 :
    해시맵, 큐
'''
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input())

graph = defaultdict(list)
dist = defaultdict(int)
for _ in range(n):
    line = list(map(int, input().split()))[:-1]
    for i in range(1, len(line), 2):
        graph[line[0]].append((line[i], line[i + 1]))


def bfs(start, graph):
    visited = set()
    queue = deque()
    queue.append((start, 0))
    farthest_node = start
    max_distance = 0

    while queue:
        node, distance = queue.popleft()
        if distance > max_distance:
            max_distance = distance
            farthest_node = node
        visited.add(node)
        for i, d in graph[node]:
            if i not in visited:
                queue.append((i, distance + d))

    return farthest_node, max_distance

fnode, _ = bfs(1,graph)
_, fdistance = bfs(fnode, graph)
print(fdistance)