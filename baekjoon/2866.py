# https://www.acmicpc.net/problem/2866

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, m, arr):
    def check(idx):
        found = set()
        for col in range(m):
            string = ""
            for row in range(idx, n):
                string += arr[row][col]
            if string in found:
                return False
            found.add(string)
        return True

    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if check(mid):
            left = mid + 1
        else:
            right = mid - 1

    return right



n, m = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(input().strip())
print(solution(n, m, arr))
