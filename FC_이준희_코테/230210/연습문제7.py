# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''
import math
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(1, n):
        for i in range(j - 1, -1, -1):
            small = sys.maxsize
            for k in range(j - i):
                small = min(small, dp[i][i + k] + dp[i + k + 1][j])  # 경우의 수들 중 최소값
            dp[i][j] = small + sum(arr[i:j + 1])  # i~ j+1까지 합
    print (dp[0][-1])



import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    dp = [[0] * n for _ in range(n)]
    f = list(map(int, input().split()))
    s = [0]
    A = [[0] * n for _ in range(n)]
    for i in range(n):
        A[i][i] = i
        s.append(s[i]+f[i])

    for z in range(1, n):
        for i in range(n-z):
            j = i + z
            dp[i][j]=sys.maxsize

            for k in range(A[i][j - 1], min(A[i + 1][j]+1,j)):
                minn = dp[i][k]+dp[k+1][j]+s[j+1]-s[i]
                if dp[i][j]>minn:
                    dp[i][j]=minn
                    A[i][j] = k
    print(dp[0][-1])

'''
(0,0)
(1,1)
(0,1)
(2,2)
(1,2)
(0,2)
(3,3)
(2,3)
(1,3)
(0,3)


'''
def solution():
    n = int(input())
    arr = [int(x) for x in input().split()]
    alist = [[0 for _ in range(n)] for _ in range(n)]
    print(*alist, sep = "\n")
    for j in range(1, n):
        for i in range(j-1,-1,-1):
            current_min = sys.maxsize
            for k in range(j-i):
                current_min = min(current_min, alist[i][i+k] + alist[i+k+1][j])
            alist[i][j] = current_min + sum(arr[i:j+1])
    print(*alist, sep = "\n")
'''
(0,4) // i=0, j=4
current_min = min(current_min, alist[i][i+k] + alist[i+k+1][j])

current_min = min(current_min, alist[0][0] + alist[1][5])
current_min = min(current_min, alist[0][1] + alist[2][5])
current_min = min(current_min, alist[0][2] + alist[3][5])
current_min = min(current_min, alist[0][3] + alist[4][5])
current_min = min(current_min, alist[0][4] + alist[5][5])

current_min = min(current_min, (A~A) + (B~F))
current_min = min(current_min, (A~B) + (C~F))
current_min = min(current_min, (A~C) + (D~F))
current_min = min(current_min, (A~D) + (E~F))
current_min = min(current_min, (A~E) + (F~F))

'''

for i in range(500):
    if 2**i-2 >= 200000000:
        print(i)
        break

