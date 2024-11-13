# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
import heapq
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(n):
    min_heap = []
    for i in range(n):
        num = int(input())
        if num == 0:
            if min_heap:
                print(heapq.heappop(min_heap)[1])
            else:
                print(0)
        else:
            heapq.heappush(min_heap, [abs(num), num])

if __name__ == '__main__':
    solution(int(input().rstrip()))
