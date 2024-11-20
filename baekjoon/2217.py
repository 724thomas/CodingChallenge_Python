# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
input = lambda: sys.stdin.readline().rstrip()

def solution(n, ropes):
    return max([ropes[i] * (i+1) for i in range(len(ropes))])

if __name__ == '__main__':
    n = int(input())
    ropes = sorted([int(input()) for _ in range(n)], key=lambda x: -x)
    print(solution(n, ropes))