# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''
import math
import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(n, cities):
    total = sum(b for a, b in cities)
    curr = 0
    target = math.ceil(total/2)

    for city, pop in cities:
        curr += pop
        if curr >= target: return city


if __name__ == '__main__':
    n = int(input())
    cities = sorted([list(map(int, input().split())) for _ in range(n)]);
    print(solution(n, cities))