# https://www.acmicpc.net/problem/14425

'''
1. 아이디어 :
    1) set을 이용하여 입력값을 받고, 입력값을 하나씩 확인하면서 set에 있는지 확인한다.
2. 시간복잡도 :
    1) O(n) + O(m) = O(n)
    - n개의 원소를 set에 넣고, m개의 원소를 확인(1)
3. 자료구조 :
    1) set
'''

import sys
n ,m = map(int, sys.stdin.readline().split())
base = set()
for _ in range(n):
    base.add(sys.stdin.readline().strip())
count = 0
for _ in range(m):
    if sys.stdin.readline().strip() in base:
        count += 1
print(count)