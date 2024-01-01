# https://www.acmicpc.net/problem/26168 배열 전체 탐색하기

'''
1. 아이디어 :
    >= arr의 원소중 k보다 크거나 같은 원소의 개수. (k보다 작은 숫자 + 1의 인덱스)
    > arr의 원소중 k보다 큰 원소의 개수 (k보다 큰 다음 수의 인덱스)
2. 시간복잡도 :
    O(nlogn)
3. 자료구조 :
    배열
'''
import sys

sys.setrecursionlimit(1000000)

input = sys.stdin.readline


def sol1(k, arr):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= k:
            right = mid
        else:
            left = mid + 1

    return len(arr) - left


def sol2(k, arr):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] > k:
            right = mid
        else:
            left = mid + 1

    return len(arr) - left


n, m = list(map(int, input().split()))
arr = [int(num) for num in input().split()]

for _ in range(m):
    commands = list(map(int, input().split()))
    if commands[0] == 1:
        print(sol1(commands[1], arr))

    elif commands[0] == 2:
        print(sol2(commands[1], arr))

    else:
        small = sol1(commands[1], arr)
        big = sol2(commands[2], arr)
        print(small-big)

