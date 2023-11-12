# https://www.acmicpc.net/problem/11437

'''
1. 아이디어 :
    LCA문제다.
    1. 모든 노드에 대한 깊이를 계산
    2. 최소 공통 조상을 찾을 두 노드 확인
        - 두 노두의 depth가 동일해지도록 거슬러 올라간다
        - 부모가 같아질때까지 두 노드를 거슬러 올라간다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    2차 배열
'''
import sys

sys.setrecursionlimit(10 ** 9)

n = int(input())
dp = [0 for i in range(n + 1)]
par = [0 for i in range(n + 1)]
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(n - 1):
    x, y = list(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)


def find_depth(node, depth):
    visited[node] = True
    dp[node] = depth

    for n in graph[node]:
        if visited[n]:
            continue
        par[n] = node
        find_depth(n, depth + 1)

def lca(a, b):
    while True:
        if dp[a] == dp[b]:
            break
        elif dp[a] > dp[b]:
            a = par[a]
        elif dp[b] > dp[a]:
            b = par[b]

    while a!=b:
        a = par[a]
        b = par[b]

    return a



find_depth(1, 1)

for i in range(int(input())):
    a, b = list(map(int, input().split()))
    print(lca(a, b))

# print(nodes)
# print(dp)
# print(par)
