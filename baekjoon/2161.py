# https://www.acmicpc.net/problem/2161

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''
import sys
from collections import deque
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input().rstrip())


def solution(n):
    queue = deque()
    for i in range(1, n+1):
        queue.append(i)

    while len(queue) != 1:
        print(queue.popleft())
        queue.append(queue.popleft())
    print(queue[0])



solution(n)
