# https://www.acmicpc.net/problem/9095

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys
year = int(sys.stdin.readline())
print(1 if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 else 0)

