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
    # print(*arr, sep="\n")

    arr.sort()
    # print(arr)
    ans = 0
    while len(arr) >= 3:
        ans += arr.pop()
        ans += arr.pop()
        arr.pop()
    # print(arr, ans)
    ans += sum(arr)
    return ans


if __name__ == '__main__':
    # n, m = map(int, input().split())
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    print(solution(n, arr))
