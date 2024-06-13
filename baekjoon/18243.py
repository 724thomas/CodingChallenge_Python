# https://www.acmicpc.net/problem/18243

'''
1. 아이디어 :
    bfs를 통해서 6까지만 방문하고 visited에 모두 방문됬는지 확인
2. 시간복잡도 :
    O( n^^2 )
3. 자료구조 :
    해시맵
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict, deque


def solution(n, k, rel):
    graph = defaultdict(list)
    for u, v in rel:
        graph[u].append(v)
        graph[v].append(u)

    def bfs(start):
        visited = set()
        visited.add(start)
        queue = deque()
        queue.append((start, 0))
        steps = defaultdict(int)
        steps[start] = 0

        while queue:
            curr, step = queue.popleft()
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    if step + 1 > 6:
                        return False
                    visited.add(neighbor)
                    queue.append((neighbor, step + 1))
                    steps[neighbor] = step + 1
        return len(visited) == n

    for i in range(1, n + 1):
        if not bfs(i):
            return "Big World!"
    return "Small World!"


n, k = list(map(int, input().split()))
rel = []
for _ in range(k):
    rel.append(list(map(int, input().split())))
print(solution(n, k, rel))


# http://colorscripter.com/s/OrZcT55