# https://www.acmicpc.net/problem/2839

'''
1. 아이디어 :
    dp문제
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열
'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n):
    dp = [10e6] * (n+1)
    dp[0] = 0

    for i in range(3, n+1):
        if i >= 3:
            dp[i] = min(dp[i], dp[i-3] + 1)
        if i >= 5:
            dp[i] = min(dp[i], dp[i-5] + 1)

    return dp[n] if dp[n] != 10e6 else -1

n = int(input())
print(solution(n))


