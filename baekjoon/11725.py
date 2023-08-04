# https://www.acmicpc.net/problem/11725

'''
1. 아이디어 :
    BFS
2. 시간복잡도 :
    O(N)
3. 자료구조 :
    뱌열 (그래프)
'''


from collections import deque

N = int(input())
graph = [[] for i in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)

ans = [0]*(N+1)

def bfs():
    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if ans[nxt] == 0:
                ans[nxt] = now
                queue.append(nxt)

bfs()
res = ans[2:]
for x in res:
    print(x)