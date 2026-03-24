# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys
input = sys.stdin.readline

n = int(input())
a, b, c = map(int, input().split())

max_dp = [a, b, c]
min_dp = [a, b, c]

for _ in range(n - 1):
    a, b, c = map(int, input().split())

    new_max0 = max(max_dp[0], max_dp[1]) + a
    new_max1 = max(max_dp[0], max_dp[1], max_dp[2]) + b
    new_max2 = max(max_dp[1], max_dp[2]) + c

    new_min0 = min(min_dp[0], min_dp[1]) + a
    new_min1 = min(min_dp[0], min_dp[1], min_dp[2]) + b
    new_min2 = min(min_dp[1], min_dp[2]) + c

    max_dp = [new_max0, new_max1, new_max2]
    min_dp = [new_min0, new_min1, new_min2]

print(max(max_dp), min(min_dp))

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