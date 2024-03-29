# https://www.acmicpc.net/problem/11286

'''
1. 아이디어 :
    1)  절대값이 작은 순서대로 정렬한다.
2. 시간복잡도 :
    1)  O(n) * O(logn) = O(nlogn)
        입력받는 횟수 * Heappush, Heappoop의 시간복잡도
3. 자료구조 :
    1) 힙
'''

import heapq
import sys
input = sys.stdin.readline


heap = []
for i in range(int(input())):

        num = int(input())

        if num == 0:
            if len(heap) == 0:
                print(0)
            else:
                print(heapq.heappop(heap)[1])
        else:
            heapq.heappush(heap, (abs(num), num))
