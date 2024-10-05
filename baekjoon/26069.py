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

def solution(n):
    dancing = set()
    dancing.add("ChongChong")
    for _ in range(n):
        s1, s2 = input().split(" ")
        if (s1 in dancing or s2 in dancing):
            dancing.add(s1)
            dancing.add(s2)
    return len(dancing)


if __name__ == '__main__':
    n = int(input())
    print(solution(n))
