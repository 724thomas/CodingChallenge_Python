# https://www.acmicpc.net/problem/1094 막대기

'''
1. 아이디어 :
    스택을 사용해봤다
2. 시간복잡도 :
    O(7)
3. 자료구조 :
    스택
'''
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n):
    nums = [1, 2, 4, 8, 16, 32, 64]
    count = 0
    while n:
        num = nums.pop()
        if num <= n:
            n -= num
            count += 1
    return count


n = int(input().rstrip())
print(solution(n))
