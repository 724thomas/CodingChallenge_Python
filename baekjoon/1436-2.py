# https://www.acmicpc.net/problem/1436 영화감독 숌

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(num):
    start = 665
    while num:
        start += 1
        if '666' in str(start):
            num -= 1
    return start

n = int(input().rstrip())
print(solution(n))
