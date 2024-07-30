# https://www.acmicpc.net/problem/17216

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

from bisect import bisect_left
def solution(n, arr):
    # print(*arr, sep="\n")
    dp = [0] * n
    for i in range(n):
        dp[i] = arr[i]

    for i in range(1, n):
        for j in range(i):
            if arr[j] > arr[i]:
                dp[i] = max(dp[i], dp[j] + arr[i])
    return max(dp)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(solution(n, arr))


