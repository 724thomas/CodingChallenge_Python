# https://www.acmicpc.net/problem/11931

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
print(*sorted([int(input().rstrip()) for _ in range(n)], reverse=True), sep= '\n')