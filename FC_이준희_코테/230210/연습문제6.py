# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
pal_list = [[0] * n for _ in range(n)]

#문자 1개, 2개 체크
for i in range(n - 1):
    pal_list[i][i] = 1
    if nums[i] == nums[i + 1]:
        pal_list[i][i + 1] = 1
pal_list[n-1][n-1] = 1

#나머지 문자 3개 이상 체크
for i in range(2, n):
    for j in range(n - i):
        if nums[j] == nums[i + j] and pal_list[j + 1][i + j - 1]:
            pal_list[j][j + i] = 1

for _ in range(int(input())):
    s, e = map(int, input().split())
    print(pal_list[s - 1][e - 1])
