# https://www.acmicpc.net/problem/22947

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

from itertools import combinations
from collections import defaultdict
import heapq


def solution(n, k, ttimes, arr):
    # print(*arr, sep="\n")

    def get_time(times):
        degrees = ddegrees.copy()
        total_degrees = sum(degrees)
        min_heap = [(times[0], 0)]
        last_node = float('inf')

        while min_heap:
            time, curr = heapq.heappop(min_heap)
            if total_degrees == 0:
                last_node = min(last_node, time - times[curr] + ttimes[curr])

            for post in pres[curr]:
                degrees[post] -= 1
                total_degrees -= 1
                if degrees[post] == 0:
                    heapq.heappush(min_heap, (time + times[post], post))
        return last_node

    comb_temp = [i for i in range(1, n)]
    pres = defaultdict(list)
    ddegrees = [0 for _ in range(n)]
    for u, v in arr:
        ddegrees[v - 1] += 1
        pres[u - 1].append(v - 1)
    ans = float('inf')
    for comb in combinations(comb_temp, k):
        times = ttimes.copy()
        for i in comb:
            times[i] = 0
        ans = min(ans, get_time(times))

    return ans


if __name__ == '__main__':
    n, m, k = list(map(int, input().strip().split()))
    times = list(map(int, input().strip().split()))
    arr = [list(map(int, input().strip().split())) for _ in range(m)]
    print(solution(n, k, times, arr))
