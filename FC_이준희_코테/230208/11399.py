# https://www.acmicpc.net/problem/11399

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


import sys
input = sys.stdin.readline
people = int(input())
times = sorted(list(map(int, input().split())))

ans = 0
temp = [times[0]]
for i in range(1, people):
    temp.append(temp[i-1] + times[i])
print(sum(temp))

