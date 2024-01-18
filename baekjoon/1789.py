# https://www.acmicpc.net/problem/1789  수들의 합

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input().rstrip())


def solution(n):

    i = 1
    while n - i >= 0:
        n -= i
        i += 1

    return i-1

print(solution(n))
