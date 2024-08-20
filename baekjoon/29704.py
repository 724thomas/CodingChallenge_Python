# https://www.acmicpc.net/problem/29704

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys
input = lambda: sys.stdin.readline().rstrip()

def solution(n, m, problems):
    problems.sort(key=lambda x: (-x[1], x[0]))
    dp = [0] * (m + 1)
    # print(problems)
    for dur, money in problems:
        for t in range(m, dur - 1, -1):
            dp[t] = max(dp[t], dp[t - dur] + money)
            # print(dp)

    total_penalty = sum(penalty for _, penalty in problems)
    return total_penalty - dp[m]

if __name__ == '__main__':
    n, m = map(int, input().split())
    problems = [tuple(map(int, input().split())) for _ in range(n)]
    print(solution(n, m, problems))

