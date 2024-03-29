# https://www.acmicpc.net/problem/7662

'''
1. 아이디어 :
    1)  최대힙, 최소힙, 해시맵을 사용한다.
        해시맵에서는 입력된 숫자의 남아있는 갯수를 추적하기 위해 만들었다.
        힙에서 값이 삭제 될때, 해시맵에서 값이 0이면 다음 값을 삭제.
        삭제할 값의 갯수가 1이상이면 1 차감한다.
        마지막에 해시맵에 남아있는 숫자 중, 1이상인 애들의 최소, 최대를 구한다.
2. 시간복잡도 :
    1)  O(test_case) + O(c) * O(k) * O(logn) + O(k) = O(커멘드 * k * logn)
        테스트 케이스 갯수 + 커멘드 * 힙 길이 * HeapPush/POP + 해시맵 순회
3. 자료구조 :
    1) 힙, 해시맵
'''

import heapq
import sys

input = sys.stdin.readline

for test_cases in range(int(input())):
    commands = int(input())

    numlist = {}
    min_heap = []
    max_heap = []
    for _ in range(commands):
        command, num = input().split()
        num = int(num)
        # print(command, num)
        if command == "I":
            # Insert
            numlist[num] = numlist.get(num, 0) + 1
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        else:
            if num == 1:  # Delete max
                while max_heap and numlist.get(-max_heap[0], 0) <= 0:  # numlist에 값이 있을때까지
                    heapq.heappop(max_heap)
                try:
                    del_num = -heapq.heappop(max_heap)
                    numlist[del_num] -= 1
                except:
                    pass

            elif num == -1:  # Delete min
                while min_heap and numlist.get(min_heap[0], 0) <= 0:  # numlist에 값이 있을떄까지
                    heapq.heappop(min_heap)
                try:
                    del_num = heapq.heappop(min_heap)
                    numlist[del_num] -= 1
                except:
                    pass

        # print("result", min_heap, max_heap, numlist)
        # print("------------------")

    cmin = sys.maxsize
    cmax = -sys.maxsize
    for key, val in numlist.items():
        if val != 0:
            cmax = max(cmax, key)
            cmin = min(cmin, key)

    if cmin == sys.maxsize:
        print("EMPTY")
    else:
        print(cmax, cmin)

'''
7
I 16
I 10
D -1
D 1
D 1
I 123
D -1
'''
