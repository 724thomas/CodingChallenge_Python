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

def solution(n, A, m, B):
    a_idx = b_idx = 0
    ans = []

    while True:
        found = False

        for num in range(100, 0, -1):
            next_a = next_b = -1

            for i in range(a_idx, n):
                if A[i] == num:
                    next_a = i
                    break

            if next_a == -1:
                continue

            for i in range(b_idx, m):
                if B[i] == num:
                    next_b = i
                    break

            if next_b == -1:
                continue

            ans.append(num)
            a_idx = next_a + 1
            b_idx = next_b + 1
            found = True
            break

        if not found:
            break

    print(len(ans))
    if ans:
        print(*ans)



if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))
    solution(n, A, m, B)

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