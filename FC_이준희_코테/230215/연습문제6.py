# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''
def binarySearch(list, target):
    start = 0
    end = len(list)-1
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == target:
            return 1
        elif list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

import sys
input = sys.stdin.readline

n = int(input())
nnums = sorted(list(map(int,input().split())))
m = int(input())
mnums = list(map(int, input().split()))
for i in mnums:
    print(binarySearch(nnums,i))