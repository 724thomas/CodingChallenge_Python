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


def solution(n, m, arr):
    concluded = [[0] + [float("-inf")] * m for _ in range(n + 1)]
    notConcluded = [[0] + [float("-inf")] * m for _ in range(n + 1)]

    for i in range(1, n+1):
        num = arr[i-1]
        for parts in range(1, m+1):
            notConcluded[i][parts] = max(concluded[i-1][parts], notConcluded[i-1][parts])
            concluded[i][parts] = max(notConcluded[i-1][parts-1], concluded[i-1][parts]) + num
    return max(concluded[n][m], notConcluded[n][m])

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    print(solution(n, m, arr))

