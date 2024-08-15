# https://www.acmicpc.net/problem/

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

def solution(arr):
    n = len(arr)

    dp = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(n+1)]

    for i in range(1, n+1):
        w, b = arr[i-1]
        for j in range(16):
            for k in range(16):
                # 현재 플레이어를 선택X
                dp[i][j][k] = dp[i-1][j][k]
                # 백 플레이어로 선택
                if j > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][k] + b)
                # 흑 플레이어로 선택
                if k > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1] + w)

    # print(*dp[n], sep='\n')

    return dp[n][15][15]

if __name__ == '__main__':
    arr = []
    while True:
        val = list(map(int, input().split()))
        if not val:
            break
        arr.append(val)
    print(solution(arr))

