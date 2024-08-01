# https://www.acmicpc.net/problem/16432

'''
1. 아이디어 :
    2차 dp
2. 시간복잡도 :
    O( n * 9 * 9)
3. 자료구조 :
    배열
'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()


def solution(arr):
    n = len(arr)
    dp = [[["", -1] for _ in range(10)] for _ in range(n)]
    for i in range(len(arr[0])):
        dp[0][arr[0][i]] = [str(i + 1), arr[0][i]]

    for day in range(1, n):
        for num in arr[day]:
            for i in range(1, 10):
                if num == i or dp[day - 1][i][0] == "":
                    continue
                s, prev = dp[day - 1][i]
                dp[day][num] = [s + str(prev), num]
    print(*dp, sep='\n')
    for i in range(10):
        if dp[-1][i][0] != "":
            prev, curr = dp[-1][i]
            ans = prev[1:] + str(curr)
            for c in ans:
                print(int(c))
            exit()

    print(-1)


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().strip().split()))[1:])
    solution(arr)
