# https://www.acmicpc.net/problem/1343

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

s = input().rstrip()


def solution(s):
    s = s.split(".")
    ans = ""
    print(s)
    for i in range(len(s)):
        if len(s[i]) % 2 == 1:
            return -1
        else:
            ans += "B" * len(s[i])+"."
    ans = ans.replace("BBBB", "AAAA")
    return ans[:-1]

print(solution(s))
