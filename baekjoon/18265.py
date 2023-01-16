# https://www.acmicpc.net/problem/18265

'''
1. 아이디어 :
    nums에 1부터 N까지 %3!=0 and %5!=0인 수를 넣는다.
2. 시간복잡도 :
    1) O(n)
3. 자료구조 :
    1) 배열
'''

import sys

input = sys.stdin.readline
n = int(input())
count = 0
for i in range(1000000000):
    if i % 3 != 0 and i % 5 != 0:
        count += 1
    if count == n:
        print(i)
        break

