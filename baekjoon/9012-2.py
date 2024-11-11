# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(s):
    stack = []
    for c in s:
        if not stack and c == ")": return "NO";

        if not stack or c == "(":
            stack.append(c)
        else: # )
            if stack[-1] == "(":
                stack.pop()
    return "YES" if len(stack)==0 else "NO"



if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = input().strip()
        print(solution(s))
