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

def solution(n, drinks):
    total = drinks[-1]
    for i in range(len(drinks)-1):
        total += drinks[i]/2
    return total



if __name__ == '__main__':
    n = int(input())
    drinks = sorted(list(map(int, input().split())))
    print(solution(n, drinks))