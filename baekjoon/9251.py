# https://www.acmicpc.net/problem/9251 LCS

'''
1. 아이디어 :
    dp 문제
2. 시간복잡도 :
    O(n^2)
3. 자료구조 :
    배열
'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


s1 = input().rstrip()
s2 = input().rstrip()

def solution(s1, s2):
    dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]

    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s2)-1,-1,-1):
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])

    return dp[0][0]


print(solution(s1, s2))