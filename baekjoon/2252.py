# https://www.acmicpc.net/problem/2252

'''
1. 아이디어 :
    map을 통해 우선순위를 구하고, 큐를 통해 bfs
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵, 배열
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict, deque
def solution(m, edges):
    map = defaultdict(list)
    counter = [0] * (m+1)
    queue = deque()

    for u, v in edges:
        map[u].append(v)
        counter[v] += 1

    for i in range(1, m+1):
        if counter[i] == 0:
            queue.append(i)

    ans = []
    while queue:
        val = queue.popleft()
        ans.append(val)
        for neighbor in map[val]:
            counter[neighbor]-=1
            if counter[neighbor] == 0:
                queue.append(neighbor)
    return ans


n, m = list(map(int, input().split()))
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))
print(*solution(n, edges))


