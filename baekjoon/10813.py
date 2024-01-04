# https://www.acmicpc.net/problem/10813 공 바꾸기

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, m):
    bags = [i+1 for i in range(n)]
    for _ in range(m):
        a, b = list(map(int, input().split()))
        bags[a-1], bags[b-1] = bags[b-1], bags[a-1]
    return bags


n, m = list(map(int, input().split()))
print(*solution(n, m))

