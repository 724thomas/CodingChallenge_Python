# https://www.acmicpc.net/problem/1541

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys

input = sys.stdin.readline

Strings = input().strip().split('-')
for i in range(len(Strings)):
    Strings[i] = -sum(map(int, Strings[i].split('+')))
print(-Strings[0] + sum(Strings[1:]))
