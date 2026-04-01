# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 / 알고리즘 :

'''


import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(arr):

    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr[0]]

    center = [arr[0]]
    left = 1
    right = len(arr)

    while left<right:
        mid = (left + right) // 2
        if arr[mid] < center[0]:
            left = mid + 1
        else:
            right = mid
    left = solution(arr[1:right])
    right = solution(arr[right:])
    return left+right+center



if __name__ == '__main__':
    arr = []
    while True:
        try:
            arr.append(int(sys.stdin.readline()))
        except:
            break
    ans = solution(arr)
    for a in ans:
        print(a)


# n = int(input().rstrip())
#
# n, m = map(int, input().split())
# n, m = list(map(int, input().split()))
# a = [c for c in input().strip()]
#
# s = input().rstrip()

# arr = list(map(int, input().strip().split()))
# arr = tuple(map(int, input().split()))
# integer_list = [int(num) for num in input().split()]
# dp = [[0 for _ in range(n)] for _ in range(n)]
# dp = [[0 for j in range(n)] for i in range(n)]
# grid = [list(input().rstrip()) for _ in range(n)] # "aaa" "bbb"
# grid = list(list(map(int, input().split())) for _ in range(n)) # "0 0 0 0", "0 0 0 0"