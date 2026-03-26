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

def solution(n, arr):
    dp = [0] * (n+2)

    for day in range(n, 0, -1):
        time, price = arr[day]

        dp[day] = dp[day+1] # 상담X

        if day + time <= n+1: # 상담O
            dp[day] = max(dp[day], price + dp[day+time])
    return dp[1]

if __name__ == '__main__':
    n = int(input())
    arr = [(0,0)]
    for _ in range(n):
        t, p = map(int, input().split())
        arr.append((t, p))
    print(solution(n, arr))

# n = int(input().rstrip())
#
# n, m = map(int, input().split())
# n, m = list(map(int, input().split()))
# a = [c for c in input().strip()]
#
# s = input().rstrip()

# arr = list(map(int, input().strip().split()))
# arr = tuple(map(int, input().split()))
# integer_list = [int(num) for num in input().split()]
# dp = [[0 for _ in range(n)] for _ in range(n)]
# dp = [[0 for j in range(n)] for i in range(n)]
# grid = [list(input().rstrip()) for _ in range(n)] # "aaa" "bbb"
# grid = list(list(map(int, input().split())) for _ in range(n)) # "0 0 0 0", "0 0 0 0"