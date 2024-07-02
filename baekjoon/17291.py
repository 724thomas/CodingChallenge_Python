# https://www.acmicpc.net/problem/17291

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict


def solution(n):
    dies = defaultdict(int)

    bugs = 1
    dies[4] = 1
    for year in range(2, n + 1):
        dies[year + 4 - year % 2] += bugs
        bugs *= 2
        bugs -= dies[year]
    return bugs

    ans = 1
    return ans


n = int(input())
print(solution(n))
