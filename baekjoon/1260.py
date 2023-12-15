# https://www.acmicpc.net/problem/1260

'''
1. 아이디어 :
    그래프 정렬 후 dfs, bfs
2. 시간복잡도 :
    O(V+E)
3. 자료구조 :
    해시맵
'''
from collections import defaultdict
from collections import deque
import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = defaultdict(list)

edges = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()



def dfs(node):
    visited[node] = True
    print(node, end=' ')
    for i in graph[node]:
        if not visited[i]:
            dfs(i)


def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
