# https://www.acmicpc.net/problem/7567 그릇

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(s):
    ans = 0
    dir = ""
    for b in s:
        if b == dir:
            ans += 5
        else:
            ans += 10
            dir = b

    return ans



s = input().rstrip()

print(solution(s))
