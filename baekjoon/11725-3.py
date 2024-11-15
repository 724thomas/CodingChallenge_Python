# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
from collections import defaultdict, deque
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(n, arr):
    graph = defaultdict(set)
    for a, b in arr:
        graph[a].add(b)
        graph[b].add(a)

    ans = [0] * (n+1)
    queue = deque()
    visited = set()
    queue.append(1)
    visited.add(1)

    while queue:
        curr = queue.popleft()
        for child in graph[curr]:
            if child in visited: continue
            visited.add(child)
            queue.append(child)
            ans[child] = curr

    for num in ans[2:]:
        print(num)



if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n-1):
        arr.append(tuple(map(int, input().split())))
    solution(n, arr)

# n = int(input().rstrip())
#
# n, m = map(int, input().split())
# n, m = list(map(int, input().split()))
# a = [c for c in input().strip()]
#
# s = input().rstrip()

#
# arr = tuple(map(int, input().split()))
# integer_list = [int(num) for num in input().split()]
# dp = [[0 for _ in range(n)] for _ in range(n)]
# dp = [[0 for j in range(n)] for i in range(n)]
# grid = [list(input().rstrip()) for _ in range(n)] # "aaa" "bbb"
# grid = list(list(map(int, input().split())) for _ in range(n)) # "0 0 0 0", "0 0 0 0"