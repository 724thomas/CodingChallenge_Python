# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict
from heapq import heappush, heappop
def solution(n, arr):
    arr.sort(key = lambda x: x[2])
    par = [i for i in range(n+1)]
    rank = [0] * (n+1)
    edges = 0
    total = 0
    last = 0

    def find(x):
        if par[x] != x:
            par[x] = find(par[x])
        return par[x]

    def union(a, b):
        ra = find(a)
        rb = find(b)

        if (rank[ra] > rank[rb]):
            par[rb] = ra
        elif (rank[ra] < rank[rb]):
            par[ra] = rb
        else:
            par[rb] = ra
            rank[ra] +=1

    for u, v, d in arr:
        if find(u) == find(v): continue
        union(u, v)
        total += d
        last = d
        edges +=1
        if edges == n-1:
            break

    return total - last

if __name__ == '__main__':
    n, m = map(int, input().split())
    # arr = tuple(map(int, input().split()))
    arr = []
    for i in range(m):
        arr.append(list(map(int, input().split(" "))));
    print(solution(n, arr))