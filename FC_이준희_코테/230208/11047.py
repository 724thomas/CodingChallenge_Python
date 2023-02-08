# https://www.acmicpc.net/problem/11047

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


import sys
input = sys.stdin.readline

coins, target = map(int, input().split())
coin_list = [int(input()) for _ in range(coins)]
ans = 0

for coin in range(coins-1, -1, -1):
    ans += target // coin_list[coin]
    target = target % coin_list[coin]
print(ans)