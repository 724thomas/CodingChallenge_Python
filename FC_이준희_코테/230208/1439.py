# https://www.acmicpc.net/problem/1439

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys

input = sys.stdin.readline

String = input().strip()
ans = String[0]
for i in range(1, len(String)):
    if String[i - 1] != String[i]:
        ans += String[i]

print(min(ans.count('0'), ans.count('1')))
