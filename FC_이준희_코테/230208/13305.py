# https://www.acmicpc.net/problem/13305

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


import sys
input = sys.stdin.readline

cities = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
ans = 0
cmin = prices[0]
for i in range(cities-1):
    cmin = min(cmin, prices[i])
    ans += cmin * distances[i]
print(ans)

