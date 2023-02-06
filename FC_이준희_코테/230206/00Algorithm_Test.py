# https://www.acmicpc.net/problem/9095

'''
1. 아이디어 :
    1) 백트래킹으로 가능하다.
    2) 재귀함수와 Memoization을 사용한다.
    3) dp를 사용한다.
2. 시간복잡도 :
    1) O(3^n)
    2) O(n)
    3) O(n)
3. 자료구조 :
    1) 재귀함수
    2) 배열 : Memoization
    3) 배열 : dp
'''

# 1)
import sys
input = sys.stdin.readline
def backtracking(val):
    if val == n:
        global cnt
        cnt += 1
        return
    if val > n:
        return
    for i in range(1, 4):
        backtracking(val + i)
for _ in range(int(input())):
    n = int(input())
    cnt = 0
    backtracking(0)
    print(cnt)

# 2)
import sys
input = sys.stdin.readline
memoization = {}
def recursive(data):
    if (data == 1):
        return 1
    elif (data == 2):
        return 2
    elif (data == 3):
        return 4
    else:
        if data in memoization:
            return memoization[data]
        else:
            memoization[data] = recursive(data - 1) + recursive(data - 2) + recursive(data - 3)
            return memoization[data]
for _ in range((int(input()))):
    print(recursive(int(input())))

# 3)
case = int(sys.stdin.readline())
dp = {}
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4
for j in range(case):
    n = int(sys.stdin.readline())
    for i in range(4, n + 1):
        if i not in dp:
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
    print(dp[n])
