# https://www.acmicpc.net/problem/2012

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


import sys
input = sys.stdin.readline
nums = sorted([int(input()) for _ in range(int(input()))])
ans = sum([abs(nums[i] - (i + 1)) for i in range(len(nums))])
print(ans)

'''
1 5 3 1 2
1 1 2 3 5
1 2 3 4 5
0 1 1 1 0
'''
