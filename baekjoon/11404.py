# https://www.acmicpc.net/problem/

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

def solution(n, arr):
    for mid in range(n):
        arr[mid][mid] = 0
        for start in range(n):
            for end in range(n):
                if arr[start][end] > arr[start][mid] + arr[mid][end]:
                    arr[start][end] = arr[start][mid] + arr[mid][end]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == float('inf'): arr[i][j] = 0
    for a in arr:
        print(*a)

if __name__ == '__main__':
    n = int(input())
    arr = [[float('inf')]* n for _ in range(n)]
    for _ in range(int(input())):
        a, b, c = list(map(int, input().split()))
        arr[a-1][b-1] = min(arr[a-1][b-1], c)
    solution(n, arr)
