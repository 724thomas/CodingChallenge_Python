# https://www.acmicpc.net/problem/1158

'''
1. 아이디어 :
    deque를 이용하여 구현
2. 시간복잡도 :
    O(n^2)
3. 자료구조 :
    deque
'''

from collections import deque
import sys

input = sys.stdin.readline

n, m = 7, 3 #map(int, input().split())  # n : 큐의 크기, m : 뽑아내려는 수의 개수
d = deque([i for i in range(1, n + 1)])  # 1부터 n까지의 수를 deque에 넣음

ans = []
while d:
    for _ in range(m - 1):
        d.append(d.popleft())
    ans.append(str(d.popleft()))

print("<"+", ".join(ans)+">")