# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    값들을 기준으로 최대 이익을 계산한다
2. 시간복잡도 :
    O( n**2)
3. 자료구조 :
    배열
'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()


def solution(n, arr):
    def calc(cost):
        money = 0
        for will, delivery in arr:
            if will >= cost:
                profit = cost - delivery
                if profit > 0:
                    money += profit
        return money

    candids = [will[0] for will in arr]
    cmax = 0
    ans = 0
    for candid in candids:
        total = calc(candid)
        if total > cmax:
            cmax = total
            ans = candid
        elif total == cmax:
            ans = min(ans, candid)

    return ans


if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().strip().split())) for _ in range(n)]
    print(solution(n, arr))
