# https://www.acmicpc.net/problem/20300

'''
1. 아이디어 :
    정렬 후, 큐를 사용해서, 개수가 홀수면 가장 마지막꺼를 제외하고, 가장 싼거 + 비싼거로 최대값을 갱신한다.
    홀수면 마지막꺼와 비교해서 최대값 갱신
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    큐
'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import deque
def solution(n, arr):
    arr.sort()
    queue = deque(arr)
    last = 0
    if len(arr) % 2 == 1:
        last = queue.pop()

    cmax = 0
    for i in range(len(queue)//2):
        cmax = max(cmax, queue.popleft() + queue.pop())

    cmax = max(cmax, last)

    return cmax

n = int(input())
arr = list(map(int, input().strip().split()))
print(solution(n, arr))


