# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict, Counter


def solution(string):
    n = len(string)
    c = Counter(string)

    ans = [0]

    def backtrack(s, size):
        if size == n:
            ans[0] += 1
            return

        for k, v in c.items():
            if v > 0 and s[-1] != k:
                c[k] -= 1
                backtrack(s + k, size + 1)
                c[k] += 1

    for k, v in c.items():
        c[k] -= 1
        backtrack(k, 1)
        c[k] += 1

    return ans[0]


if __name__ == '__main__':
    # n, m = map(int, input().split())
    # arr = tuple(map(int, input().split()))
    s = input().strip()
    print(solution(s))
