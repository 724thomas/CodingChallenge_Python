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
from collections import defaultdict

def solution(n, m, arr):
    loadable = [m] * (n+1)
    arr.sort(key=lambda x: (x[1], x[0]))
    ans = 0

    for s, e, a in arr:
        cmin = min(loadable[s : e])
        for i in range(s, e):
            loadable[i] -= min(cmin, a)
        ans += min(cmin, a)
    return ans


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []
    for i in range(int(input())):
        arr.append(list(map(int, input().split())))
    print(solution(n, m, arr))
