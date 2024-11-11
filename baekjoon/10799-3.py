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
    total, size = 0, 0

    for i, val in enumerate(s):
        if not stack or val == "(":
            stack.append([i, val]) # idx, value
            size+=1
        else:
            size-=1
            total += size if i - stack[-1][0] == 1 else 1
            stack.pop()

    return total



if __name__ == '__main__':
    s = input().strip()
    print(solution(s))
