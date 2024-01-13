# https://www.acmicpc.net/problem/10809 알파벳 찾기

'''
1. 아이디어 :

2. 시간복잡도 :
    O( 1 )
3. 자료구조 :

'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
from collections import defaultdict

def solution(s):
    hmap = defaultdict(int)
    for i in range(len(s)):
        if s[i] not in hmap:
            hmap[s[i]] = i
    ans = []
    for i in range(26):
        if chr(i + 97) in hmap:
            ans.append(hmap[chr(i + 97)])
        else:
            ans.append(-1)

    return ans

s = input().rstrip()

print(*solution(s))
