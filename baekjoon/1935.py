# https://www.acmicpc.net/problem/1935

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, s, arr):
    dict = {chr(i+65) : arr[i] for i in range(len(arr))}
    stack = []

    for i, c in enumerate(s):
        if c not in "+-*/":
            stack.append(dict[c])
        else:
            right = stack.pop()
            left = stack.pop()
            if c == "+":
                stack.append(left+right)
            elif c == "-":
                stack.append(left-right)
            elif c == "*":
                stack.append(left*right)
            elif c == "/":
                stack.append(left/right)
    return "{:.2f}".format(stack[0])


    ans = 1
    return ans


n = int(input())
s = input().strip()
arr = []
for _ in range(n):
    arr.append(int(input()))
print(solution(n, s, arr))
