# https://www.acmicpc.net/problem/2753

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys

input = sys.stdin.readline


def s_palindrome(str):
    lp, rp = 0, len(str) - 1
    while lp < rp:
        if str[lp] == str[rp]:
            lp += 1
            rp -= 1
        elif str[lp] != str[rp]:
            return 1 if (True if str[lp + 1:rp + 1] == str[lp + 1:rp + 1][::-1] else False) or (
                True if str[lp:rp] == str[lp:rp][::-1] else False) else 2


for _ in range(int(input())):
    String = input().rstrip()
    if String == String[::-1]:
        print(0)
    else:
        print(s_palindrome(String))
