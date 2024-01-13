# https://www.acmicpc.net/problem/2675 문자열 반복

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, s):
    ans = ""
    for i in range(len(s)):
        ans += s[i] * int(n)

    return ans



for _ in range(int(input().rstrip())):
    n, s = input().rstrip().split()
    print(solution(n, s))
