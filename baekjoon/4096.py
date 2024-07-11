# https://www.acmicpc.net/problem/4096

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(nums):

    for n in nums:
        count = 0
        while n != n[::-1]:
            n = str(int(n) + 1).zfill(len(n))
            count += 1
        print(count)


nums = []
while True:
    n = input().strip()
    if n == "0":
        break
    nums.append(n)
solution(nums)
