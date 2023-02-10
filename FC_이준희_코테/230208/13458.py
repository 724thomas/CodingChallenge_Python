# https://www.acmicpc.net/problem/13458

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''
import math
import sys

input = sys.stdin.readline

rooms = int(input())
students = list(map(int, input().split()))
b, c = map(int, input().split())

ans = rooms
for i in range(len(students)):
    students[i] -= b
    ans = ans + math.ceil(students[i] / c) if students[i] > 0 else ans
print(ans)
