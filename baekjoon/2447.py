# https://www.acmicpc.net/problem/2447

'''
1. 아이디어 :
    재귀로 풀 수 있다
2. 시간복잡도 :
    O(3^n)
3. 자료구조 :
    배열
'''
import sys

input = sys.stdin.readline

n = int(input())

def stars(n):
    if n == 1:
        return ["*"]

    star = stars(n // 3)
    arr = []

    for s in star:
        arr.append(s * 3)
    for s in star:
        arr.append(s + " " * (n // 3) + s)
    for s in star:
        arr.append(s * 3)
    return arr

print("\n".join(stars(n)))
