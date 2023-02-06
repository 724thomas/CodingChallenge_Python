# https://www.acmicpc.net/problem/1110

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys
target = int(sys.stdin.readline())
num, count = target, 0
while True:
    count += 1
    num = (num % 10) * 10 + ((num // 10 + num % 10) % 10)
    if num == target:
        break
print(count)
