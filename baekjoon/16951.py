# https://www.acmicpc.net/problem/16951

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
    counter = [0] * n
    for i in range(n):
        for j in range(n):
            if i < j and arr[j] != arr[i] + (j - i) * m:
                counter[i] += 1
            if i > j and arr[j] != arr[i] - (i - j) * m:
                if arr[i] - (i - j) * m < 1:
                    counter[i] = 1001
                    break
                counter[i] += 1
        print(counter)
    return min(counter)


if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    print(solution(n, m, arr))
