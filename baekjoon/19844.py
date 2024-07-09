# https://www.acmicpc.net/problem/19844

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(s):
    words = []
    temp = ""
    for c in s:
        if c == " " or c == "-":
            if temp:
                words.append(temp)
            temp = ""
        else:
            temp += c
    if temp:
        words.append(temp)

    vowels = {'a', 'e', 'i', 'o', 'u', 'h'}
    ans = len(words)
    for word in words:
        if len(word) >= 4 and word[0] == "q" and word[1] == "u" and word[2] == "'" and word[3] in vowels:
            ans += 1
        elif len(word) >=3 and word[0] in "cjnmtsld" and word[1] == "'" and word[2] in vowels:
            ans += 1
    return ans


s = input().strip()
print(solution(s))
