# https://www.acmicpc.net/problem/18110 solved.ac

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''
import sys
import math
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input().rstrip())
if n == 0:
    print(0)
    exit()
deletes = math.floor((n*0.15)+0.5)
scores = sorted([int(input()) for _ in range(n)])
scores = scores[deletes:len(scores)-deletes]
print(math.floor((sum(scores)/(len(scores)))+0.5))
