# https://www.acmicpc.net/problem/13702 이상한 술집

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


def solution(m, drinks):

    def calc_counts(target):
        counts = 0
        for d in drinks:
            counts += d//target
        return counts

    left = 0
    right = max(drinks)-1
    while left <= right:
        mid = (left+right)//2
        if calc_counts(mid) >= m:
            left = mid + 1
        else:
            right = mid - 1
    return right


n, m = list(map(int, input().split()))
drinks = []
for _ in range(n):
    drinks.append(int(input()))

print(solution(m, drinks))
