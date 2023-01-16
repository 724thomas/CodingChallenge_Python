import sys
from collections import deque


n, k = map(int, sys.stdin.readline().split())
alist = []
for i in range(n):
    alist.append(int(sys.stdin.readline()))

count = sum(alist)//k

while True:
    ans = 0
    for num in alist:
        ans += num // count
    if ans == k:
        cmax = ans
        break
    elif ans < k:
        count-=1
print(count)
