# https://www.acmicpc.net/problem/13019

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


from collections import Counter
def solution(a, b):
    if Counter(a) != Counter(b):
        return -1
    a = a[::-1]
    b = b[::-1]
    j = 0
    size = len(a)
    for i in range(size):
        if a[i] == b[j]:
            j += 1
    return size - j


if __name__ == '__main__':
    a = input().strip()
    b = input().strip()
    print(solution(a, b))
