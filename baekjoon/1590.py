# https://www.acmicpc.net/problem/1590 캠프가는 영식

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''
import sys

sys.setrecursionlimit(1000000)

input = sys.stdin.readline

n, arrive_time = list(map(int, input().split()))


def solution(arrived, times):
    left = 0
    right = len(times) - 1
    if times[-1] < arrived:
        return -1

    while left <= right:
        mid = (left + right) // 2
        next_bus = times[mid]
        if next_bus >= arrived:
            right = mid - 1
        else:
            left = mid + 1

    wait = times[left] - arrived
    if wait < 0:
        return -1
    return wait


buses = []
for _ in range(n):
    start_time, delay, counts = list(map(int, input().split()))
    for i in range(counts):
        buses.append(start_time + (delay * i))
buses.sort()
print(solution(arrive_time, buses))
