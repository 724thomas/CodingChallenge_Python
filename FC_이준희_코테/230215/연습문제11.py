# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys

input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
ans = 100000001

lp, rp = 0, 0
total = nums[0]
while True:
    if total >= s:
        ans = min(ans, rp - lp + 1)
        total -= nums[lp]
        lp += 1
    elif total < s:
        rp += 1
        if rp == n:
            break
        total += nums[rp]
print(ans if ans != 100000001 else 0)
