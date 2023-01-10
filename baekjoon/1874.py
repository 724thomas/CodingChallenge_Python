# https://www.acmicpc.net/problem/1874

'''
1. 아이디어 :
    1) 스택을 이용한다.
2. 시간복잡도 :
    1) O(n)
    - n개의 원소를 append(1)와 pop(1)
3. 자료구조 :
    1) 스택
'''

import sys

n,  alist, pointer, ans = int(sys.stdin.readline()), [0], 1, ""
for i in range(n):
    temp = int(sys.stdin.readline())
    if temp < alist[-1]:
        print("NO")
        break
    while alist[-1] != temp:
        alist.append(pointer)
        pointer += 1
        ans += "+"
    alist.pop()
    ans += "-"
else:
    for i in ans:
        print(i)