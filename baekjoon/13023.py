# https://www.acmicpc.net/problem/13023

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''
from collections import defaultdict, deque
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

grid = defaultdict(list)
n, m = list(map(int, input().split()))
visited = [False] * (n+1)
ans = [False]

for _ in range(m):
    a, b = list(map(int, input().split()))
    grid[a].append(b)
    grid[b].append(a)

def dfs(idx, count):
    visited[idx] = True
    if count == 4:
        ans[0] = True
        return

    for i in grid[idx]:
        if not visited[i]:
            dfs(i, count+1)
            visited[i] = False

for i in range(n):
    dfs(i,0)
    visited[i] = False
    if ans[0]:
        break

print(1 if ans[0] else 0)