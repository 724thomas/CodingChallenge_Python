# https://www.acmicpc.net/problem/1753

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict
import heapq
def solution(n,k,edges):
    visited = set()
    dict = defaultdict(list)
    ans = [float('inf')] * (n+1)

    for start, dest, dist in edges:
        dict[start].append( (dest, dist) )

    min_heap = [(0, k)]
    while min_heap:
        total, curr = heapq.heappop(min_heap)
        ans[curr] = min(ans[curr], total)
        if curr in visited:
            continue
        visited.add(curr)

        for neighbor, dist in dict[curr]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (total+dist, neighbor) )

    for i in range(1, len(ans)):
        if ans[i] == float('inf'):
            ans[i] = "INF"

    return ans[1:]

n, m = list(map(int, input().split()))
k = int(input())
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))
print(*solution(n,k,edges))


