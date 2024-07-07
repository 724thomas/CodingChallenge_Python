# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import Counter
def solution(s):
    counter = Counter(s)
    for i, c in enumerate(s):
        if counter[c] == 1:
            return c + "(인덱스: " + i + ")"
    return "중복 제거 후 빈 문자열이 되었습니다."


s = input().rstrip()
print(solution(s))


