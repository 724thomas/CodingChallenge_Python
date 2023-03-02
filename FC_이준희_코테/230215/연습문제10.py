# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
lp, rp, count, total = 0, 1, 0, nums[0]

while rp < n + 1:
    if rp == n and total < m:
        break
    if total == m:
        count += 1
        total -= nums[lp]
        lp += 1
    elif total > m:
        total -= nums[lp]
        lp += 1
    elif total < m:
        total += nums[rp]
        rp += 1
print(count)
