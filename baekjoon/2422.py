# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    브루트 포스로 풀 수 있다.
    해시맵(안에 해시셋)을 사용하여 매칭되는 아이스크림들을 저장한다.
    3중 for문을 돌면서 확인한다
2. 시간복잡도 :
    O( n ** 3)
3. 자료구조 :
    해시맵, 해시셋
'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict


def solution(n, m, arr):
    forbid = defaultdict(set)
    for u, v in arr:
        forbid[u].add(v)
        forbid[v].add(u)
    ans = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if j in forbid[i] or k in forbid[i]:
                    continue
                if i in forbid[j] or k in forbid[j]:
                    continue
                if i in forbid[k] or j in forbid[k]:
                    continue
                ans += 1

    return ans


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    arr = []
    for _ in range(m):
        arr.append(list(map(int, input().split())))
    print(solution(n, m, arr))
