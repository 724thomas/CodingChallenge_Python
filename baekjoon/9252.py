# https://www.acmicpc.net/problem/9252

'''
1. 아이디어 :
    2 차원 배열로 bottom up 형식.
    s1[i] == s[j] 이면, 오른쪽아래 대각선 값에 1을 더하고,
    아니면 아래와 오른쪽 중 값의 큰 값을 더한다.
    string은 0,0 부터 시작하여 반대로 top down으로 한다.
2. 시간복잡도 :
    O( n*m )
3. 자료구조 :
    배열
'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(s1, s2):
    ans = ""
    dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]

    for i in range(len(s1)-1, -1, -1):
        for j in range(len(s2)-1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])

    i = j = 0
    ans = []
    while i<len(s1) and j<len(s2):
        if s1[i] == s2[j]:
            ans.append(s1[i])
            i += 1
            j += 1
        elif dp[i+1][j] > dp[i][j+1]:
            i+=1
        else:
            j+=1

    print(dp[0][0])
    print("".join(ans))

s1 = input().strip()
s2 = input().strip()

solution(s1, s2)


