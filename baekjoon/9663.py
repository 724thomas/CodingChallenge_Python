# https://www.acmicpc.net/problem/9663

'''
1. 아이디어 :
    유명한 백트래킹 문제이다.
2. 시간복잡도 :
    O(n!) - python3 시간초과. pypy3로 풀었다.
3. 자료구조 :
    HashSet
'''

import sys

input = sys.stdin.readline

col = set()
diag = set()  # r+c
adiag = set()  # r-c

n = int(input())
ans = []

def backtracking(r):
    if r == n:
        ans.append(1)
        return

    for c in range(n):
        if c in col or r+c in diag or r-c in adiag:
            continue

        col.add(c)
        diag.add(r+c)
        adiag.add(r-c)

        backtracking(r+1)

        col.remove(c)
        diag.remove(r+c)
        adiag.remove(r-c)

backtracking(0)
print(sum(ans))