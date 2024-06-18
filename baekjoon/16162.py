# https://www.acmicpc.net/problem/16162

'''
1. 아이디어 :

2. 시간복잡도 :
    O( n )
3. 자료구조 :

'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, a, d, notes):
    ans = 0
    start = a
    for n in notes:
        if n == start:
            ans += 1
            start += d

    return ans


n, a, d = list(map(int, input().split()))
notes = list(map(int, input().split()))
print(solution(n, a, d, notes))
