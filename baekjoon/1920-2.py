# https://www.acmicpc.net/problem/1920 수 찾기

'''
1. 아이디어 :
    해시셋
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    해시셋
'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input().rstrip())
integer_list = set([int(num) for num in input().split()])
n = int(input().rstrip())
for n in [int(num) for num in input().split()]:
    if n in integer_list:
        print(1)
    else:
        print(0)

