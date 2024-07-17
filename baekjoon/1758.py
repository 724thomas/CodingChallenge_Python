# https://www.acmicpc.net/problem/1758

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
    arr.sort(reverse=True)
    return sum([max(0, arr[i] - i) for i in range(len(arr))])

if __name__ == '__main__':
    arr = []
    n = int(input())
    for _ in range(n):
        arr.append(int(input()))
    print(solution(n, arr))


