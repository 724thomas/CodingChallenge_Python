# https://www.acmicpc.net/problem/22871

'''
1. 아이디어 :
    dp 이중포문
    dp 다익스트라

2. 시간복잡도 :
    O( n**2 )
    O( nlogn)
3. 자료구조 :
    배열
    최소힙
'''

# n**2
import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, arr):
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(n):
        for j in range(i + 1, n):
            dp[j] = min(dp[j], (j - i) * (1 + abs(arr[i] - arr[j])))

    return dp[n - 1]


n = int(input())
arr = list(map(int, input().strip().split()))
print(solution(n, arr))


# 다익스트라 (nlogn)
import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline

import heapq


def solution(n, arr):
    dp = [float('inf')] * n
    dp[0] = 0
    min_heap = [(0, 0)]

    while min_heap:
        cost, i = heapq.heappop(min_heap)

        if cost > dp[i]:
            continue

        for j in range(i + 1, n):
            cost2 = (j - i) * (1 + abs(arr[i] - arr[j]))
            ncost = max(dp[i], cost2)

            if ncost < dp[j]:
                dp[j] = ncost
                heapq.heappush(min_heap, (ncost, j))
            print(dp)
        print(min_heap)

    return dp[n - 1]


n = int(input())
arr = list(map(int, input().strip().split()))
print(solution(n, arr))
