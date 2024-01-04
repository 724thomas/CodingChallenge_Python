# https://www.acmicpc.net/problem/1654 랜선 자르기

'''
1. 아이디어 :
    이분탐색
2. 시간복잡도 :
    O(nlogn)
3. 자료구조 :
    배열
'''
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(count, integer_list):
    def check(target, arr, count):
        for n in arr:
            count -= n // target
            if count <= 0:
                return True
        return False

    left = 1
    right = max(integer_list)
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if check(mid, integer_list, count):
            ans = max(ans, mid)
            left = mid + 1
        else:
            right = mid - 1

    return ans


n, count = list(map(int, input().split()))
integer_list = [int(input()) for _ in range(n)]
print(solution(count, integer_list))
