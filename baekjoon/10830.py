# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
- 분할 정복으로 거듭제곱 수행
- A^B
    - B가 짝수면: A^(B/2) * A^(B/2)
    - B가 홀수면: A^(B//2) * A^(B//2) * A
- 행렬 곱셈 결과는 매번 1000으로 나눈 나머지 저장
2. 시간복잡도 :
- 행렬 곱셈 1번: O(N^3)
- 거듭제곱 분할정복: O(log B)
- 전체: O(N^3 log B)
3. 자료구조 / 알고리즘 :
- 2차원 리스트
- 분할 정복
- 행렬 곱셈
'''


import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()
MOD = 1_000

def multiply(a, b, n):
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            val =0
            for k in range(n):
                val += a[i][k] * b[k][j]
            result[i][j] = val % MOD
    return result

def power(matrix, exp, n):
    if exp == 1:
        return [[matrix[i][j] % MOD for j in range(n)] for i in range(n)]

    half = power(matrix, exp // 2, n)
    half_squared = multiply(half, half, n)

    if exp % 2 == 0:
        return half_squared
    else:
        return multiply(half_squared, matrix, n)

def solution():
    n, b = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    ans = power(matrix, b, n)

    for row in ans:
        print(*row)


if __name__ == '__main__':
    solution()

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