# https://www.acmicpc.net/problem/11720 숫자의 합

'''
1. 아이디어 :

2. 시간복잡도 :
    O( n )
3. 자료구조 :

'''
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline
input()
ans = 0
for n in input().rstrip():
    ans += int(n)
print(ans)
