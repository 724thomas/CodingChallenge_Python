# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys
def method(n):
    for i in range(n):
        if i + (sum([int(x) for x in str(i)])) == n:
            return i
    return 0

print(method(int(sys.stdin.readline())))

