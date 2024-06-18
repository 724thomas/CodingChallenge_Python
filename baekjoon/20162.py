# https://www.acmicpc.net/problem/20162

'''
1. 아이디어 :

2. 시간복잡도 :
    O( n )
3. 자료구조 :

'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n, scores):
    dp = [0 for _ in range(n)]

    for curr in range(n):
        dp[curr] = scores[curr]
        for prev in range(curr):
            if scores[prev] < scores[curr]:
                dp[curr] = max(dp[curr], dp[prev] + scores[curr])

    return max(dp)

n = int(input())
scores = []
for _ in range(n):
    scores.append(int(input()))
print(solution(n, scores))


