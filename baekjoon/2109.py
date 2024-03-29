# https://www.acmicpc.net/problem/2109

'''
1. 아이디어 :
    1)  그리디 문제다. 해당 날짜까지 제일 가격이 낮은 가격을 제외한다.
        예를 들어, 2일까지는 2개의 강의만 할 수 있으므로, 제일 가격이 높은 2개를 제외하고 나머지는 없앤다.
        또, 3일까지는 3개의 강의만 할 수 있으므로, 제일 가격이 높은 3개를 제외하고 나머지는 없앤다.
        Heap을 이용하여 배열의 길이(강의 수)가 해당 일수보다 높으면, 가장 작은 값 제외.
        마지막 heap 안에 남아있는 값들을 모두 더한다.
2. 시간복잡도 :
    1) O(nlogn) + O(nlogn) = O(nlogn)
        정렬 + n * (Heappush, HeapPop)
3. 자료구조 :
    1) Heap
'''

import sys
import heapq

input = sys.stdin.readline
lectures = sorted([[pay, day] for pay, day in [map(int, input().split()) for x in range(int(input()))]],
                  key=lambda x: x[1])
min_heap = []
for pay, day in lectures:
    heapq.heappush(min_heap, pay)
    if day < len(min_heap):
        heapq.heappop(min_heap)
print(sum(min_heap))
