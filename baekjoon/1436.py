# https://www.acmicpc.net/problem/1436

import sys
n = int(sys.stdin.readline())
count = 0
num = 666
while True:
    if '666' in str(num):
        count+=1
        if count == n:
            print(num)
            break
    num+=1

