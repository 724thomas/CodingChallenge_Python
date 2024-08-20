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


def solution(n, arr):
    arr.sort()
    odd = len(arr) % 2
    ans = 0
    for i in range(len(arr) // 2):
        ans += arr.pop() * 2
    if odd:
        ans += arr.pop()
    return ans


if __name__ == '__main__':
    # n, m = map(int, input().split())
    n = int(input())
    arr = list(map(int, input().split()))
    print(solution(n, arr))
