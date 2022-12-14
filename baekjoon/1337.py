# https://www.acmicpc.net/problem/1337

'''
1. 아이디어 :
    1) 들어오는 값들을 sort한 후, 두개의 포인터를 두고, 두 포인터 값이 4보다 작거나 같다면, 그 사이의 숫자들의 갯수를 세고 current max를 갱신한다.
2. 시간복잡도 :
    1) O(logn) * O(n)
    - 정렬 + while문
3. 자료구조 :
    1) 배열
'''

import sys

input = sys.stdin.readline
nums = sorted([int(input()) for _ in range(int(input()))])
print(nums)
cmax = 1
lp = 0
rp = 1
while 1:
    if rp==len(nums):
        break
    if nums[rp] - nums[lp] <= 4:
        cmax = max(cmax, rp-lp+1)
        rp += 1
    else:
        lp += 1
print(5-cmax)