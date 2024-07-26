# https://www.acmicpc.net/problem/14925
'''
1. 아이디어 :
2. 시간복잡도 :
    O(
3. 자료구조 :
'''

import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()
def solution(n, m, arr):
    cmax = 0
    for row in range(n):
        for col in range(m):
            if arr[row][col] != 0:
                arr[row][col] = -1
            else:
                arr[row][col] = 1
                cmax = 1

    for row in range(1, n):
        for col in range(1, m):
            if arr[row][col] == -1:
                continue
            if arr[row-1][col-1] >= 0 and arr[row-1][col] >= 0 and arr[row][col-1] >= 0:
                arr[row][col] = min(arr[row-1][col-1], arr[row-1][col], arr[row][col-1]) + 1
                cmax = max(cmax, arr[row][col])
    return cmax

if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().strip().split())))
    print(solution(n, m, arr))