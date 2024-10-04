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

def solution(n, arr):
    max_right = arr[-1]
    ans = 0
    for i in range(n-1, -1, -1):
        max_right = max(max_right, arr[i])
        ans += max(0, max_right - arr[i])
    return ans

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = tuple(map(int, input().split()))
        print(solution(n, arr))