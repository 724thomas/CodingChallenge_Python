# https://www.acmicpc.net/problem/1676 팩토리얼 0의 개수

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    total = str(total)
    ans = 0
    for i in range(len(total)-1, -1, -1):
        if total[i] != '0':
            break
        else:
            ans += 1
    return ans

n = int(input().rstrip())

print(solution(n))
