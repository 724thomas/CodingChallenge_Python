# https://www.acmicpc.net/problem/1956

'''
1. 아이디어 :
    플로이드 워셜
    출발에서 경유지로 갈 수 있다 AND 경유지에서 도착지로 갈 수 있다.
    -> 출발에서 도착의 거리 = 출발에서 도착 거리, 출발에서 경유 거리 + 경유에서 도착 거리
2. 시간복잡도 :
O( n ** 3 )
3. 자료구조 :
    배열
'''

import sys
input = sys.stdin.readline

n, e = list(map(int, input().split()))
distance = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for _ in range(e):
    u, v, d = map(int, input().split())
    distance[u][v] = d

for mid in range(1, n + 1):  # 경유
    for start in range(1, n + 1):  # 출발
        for end in range(1, n + 1):  # 도착
            distance[start][end] = min(distance[start][end], distance[start][mid] + distance[mid][end])

ans = float('inf')
for i in range(1, n + 1):
    ans = min(ans, distance[i][i])
print(ans if ans != float('inf') else -1)

