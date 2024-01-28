# https://www.acmicpc.net/problem/23843

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''
from collections import deque
import heapq
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = list(map(int, input().split()))
devices = [int(num) for num in input().split()]
devices.sort()

if n <= m:
    print(max(n))
    exit()

time = 0
min_heap = []
for i in range(m):
    heapq.heappush(min_heap, devices.pop())

while devices:
    print(time)
    print(min_heap)
    print(devices)
    time += heapq.heappop(min_heap)
    while min_heap and min_heap[0] <= time:
        time -= time - heapq.heappop(min_heap)
    while len(min_heap) < m and devices:
        heapq.heappush(min_heap, devices.pop())

print(time)
print(min_heap)
print(devices)
'''
8 4 4 1 1

4 7
4 1 1

time = 4
4 7 
1 1

time = 

'''
