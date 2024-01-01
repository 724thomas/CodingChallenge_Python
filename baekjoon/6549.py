# https://www.acmicpc.net/problem/6549 히스토그램에서 가장 큰 직사각형

'''
1. 아이디어 :
    stack을 사용한다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    스택
'''
import sys

sys.setrecursionlimit(1000000)
from collections import deque

input = sys.stdin.readline


def solution(arr):
    max_area = 0
    stack = []

    for index1, height1 in enumerate(arr):
        start = index1
        while stack and stack[-1][1] > height1:
            index2, height2 = stack.pop()
            max_area = max(max_area, height2 * (index1 - index2))
            start = index2
        stack.append((start, height1))

    for idx, height in stack:
        max_area = max(max_area, height * (len(arr) - idx))
    return max_area


while True:
    integer_list = deque([int(num) for num in input().split()])
    n = integer_list.popleft()
    if n == 0:
        exit(0)
    print(solution(integer_list))
