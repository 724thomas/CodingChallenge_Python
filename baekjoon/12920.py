# https://www.acmicpc.net/problem/12920

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

n, m = map(int, input().split())  # n개의 물건, 가방 최대 무게 m
items = []

# 물건 입력 처리
for _ in range(n):
    v, c, k = map(int, input().split())
    count = 1
    while k > 0:
        current_count = min(count, k)
        items.append((v * current_count, c * current_count))
        k -= current_count
        count *= 2

dp = [0] * (m + 1)

# DP 배열 갱신
for weight, value in items:
    for j in range(m, weight - 1, -1):
        dp[j] = max(dp[j], dp[j - weight] + value)

print(dp[m])