# https://www.acmicpc.net/problem/5525

'''
1. 아이디어 :
    1) 슬라이딩 윈도우를 사용하면 된다.
2. 시간복잡도 :
    1) O(n)
3. 자료구조 :
    1) 문자열
'''

from collections import deque
import sys

input = sys.stdin.readline

base = deque("I" + "OI" * int(input()))
input()
string = input()
window = deque(string[:len(base)])
count = 0

for i in range(len(base), len(string) - 1):
    if window == base:
        count += 1
    deque.popleft(window)
    window.append(string[i])
print(count)
