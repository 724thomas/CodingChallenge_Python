# https://www.acmicpc.net/problem/2750

import sys
input = sys.stdin.readline
print(*sorted([int(input()) for _ in range(int(input()))]))
