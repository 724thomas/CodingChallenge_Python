# https://www.acmicpc.net/problem/

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
def solution(arr):
    arr.sort()
    ans = 0
    graph = defaultdict(list)
    for idx, color in arr:
        graph[color].append(idx)

    for k, v in graph.items():
        arr = v
        for i in range(len(arr)):
            if i == 0:
                ans += arr[1] - arr[0]
            elif i == len(arr)-1:
                ans += arr[i] - arr[i-1]
            else:
                ans += min(arr[i] - arr[i-1], arr[i+1] - arr[i])
    return ans

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().strip().split())))
print(solution(arr))


