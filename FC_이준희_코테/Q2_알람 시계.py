# https://www.acmicpc.net/problem/2753

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


import sys
h , m = map(int, sys.stdin.readline().split())
print(str(h) + " " + str(m-45) if m>=45 else "23" + " " + str(m+15) if h==0 else str(h-1) + " " +str(m+15))
