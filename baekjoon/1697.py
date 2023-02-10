# https://www.acmicpc.net/problem/1697

import sys

start, end = map(int, sys.stdin.readline().split())
diff = abs(start - end)
count = 0
while diff != 0:
    if diff % 2 == 0:
        diff = diff // 2
    else:
        diff -=1
    count+=1
    print(diff, count)

print(count)


