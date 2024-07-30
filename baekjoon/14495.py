# https://www.acmicpc.net/problem/14495

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

def solution(n):
    if n <= 3:
        return 1
    dp = [0] * (n+1)
    dp[1] = dp[2] = dp[3] = 1
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-3]
    return dp[n]

if __name__ == '__main__':
    print(solution(int(input())))


