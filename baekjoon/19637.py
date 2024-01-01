# https://www.acmicpc.net/problem/19637 IF문 좀 대신 써줘

'''
1. 아이디어 :
    binary search
2. 시간복잡도 :
    O(nlogn)
3. 자료구조 :
    배열
'''
import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

def solution(target, values):

    left = 0
    right = len(values)
    while left < right:
        mid = (left+right)//2
        if values[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return names[left]


n, m = list(map(int, input().split()))

names = []
values = []
for _ in range(n):
    name, value = input().rstrip().split()
    names.append(name)
    values.append(int(value))

for _ in range(m):
    target = int(input())
    print(solution(target, values))


