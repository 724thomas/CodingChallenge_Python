# https://www.acmicpc.net/problem/2903

'''
1. 아이디어 :
    n * n.
    점들 사이에 새로운 점이 생기므로 n = n + (n -1)
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    -
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n):
    ans = 2
    for i in range(n):
        ans += ans-1
    return ans*ans

print(solution(int(input())))


