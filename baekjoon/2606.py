# https://www.acmicpc.net/problem/2606

'''
1. 아이디어 :
    그래프 문제
2. 시간복잡도 :
    O(V+E)
3. 자료구조 :
    해시맵
'''
from collections import defaultdict
from collections import deque
import sys

input = sys.stdin.readline

computers = int(input())
graph = defaultdict(list)
visited = [False] * (computers + 1)

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)
visited[1] = True

while queue:
    computer = queue.popleft()

    for c in graph[computer]:
        if not visited[c]:
            queue.append(c)
            visited[c] = True

print(sum(visited)-1)