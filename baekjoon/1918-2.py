# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()


def solution(s):
    ans = ""
    stack = []
    operators = {"(": 0, ")": 0, "+": 1, "-": 1, "*": 2, "/": 2}

    for c in s:
        if c.isalpha():
            ans += c
        elif c == "(":
            stack.append(c)
        elif c == ")":
            while stack and stack[-1] != "(":
                ans += stack.pop()
            stack.pop()
        else:
            while stack and operators[stack[-1]] >= operators[c]:
                ans += stack.pop()
            stack.append(c)

    while stack:
        ans += stack.pop()

    return ans


if __name__ == '__main__':
    s = input().strip()
    print(solution(s))
