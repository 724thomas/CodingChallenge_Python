# https://www.acmicpc.net/problem/1912

'''
1. 아이디어 :
    1) dp문제다. 누적합 배열을 만들어서, 해당 인덱스까지의 최대합을 저장하면된다. 점화식은 다음과 같다.
    dp[i] = max(dp[i-1] + nums[i], nums[i])
2. 시간복잡도 :
    1) O(n)
3. 자료구조 :
    1) 배열
'''

import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
dp = [nums[0]] + [0] * (n-1)
for i in range(1, n):
    dp[i] = max(dp[i - 1] + nums[i], nums[i])
print(max(dp))
