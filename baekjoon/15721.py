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

from collections import deque


def solution(n, target, s):
    # 뻔 – 데기 – 뻔 – 데기 – 뻔 – 뻔 – 데기 – 데기
    # 뻔 – 데기 – 뻔 - 데기 – 뻔 – 뻔 – 뻔 – 데기 – 데기 – 데기
    count = -1
    pre = [0, 1, 0, 1]
    arr = []
    for i in range(target//2):
        arr += pre + ([0] * (i+2)) + ([1] * (i+2))

    for num in arr:
        count += 1
        if num == s:
            target -= 1
        if target == 0:
            return count % n


if __name__ == '__main__':
    n = int(input())
    target = int(input())
    s = int(input())
    print(solution(n, target, s))
