# https://www.acmicpc.net/problem/1016

'''
1. 아이디어 :
    에라토스테네스의 체를 활용
    check를 0부터 만들게되면 메모리초과.
2. 시간복잡도 :
    O( n**2 )
3. 자료구조 :
    배열
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(min_val, max_val):
    range_size = max_val - min_val + 1
    check = [True] * range_size

    max_check = int(max_val**0.5) + 1 # 10

    for i in range(2, max_check): #2~10
        square = i*i
        start = max(square, (min_val + square - 1) // square * square)

        for j in range(start, max_val + 1, square):
            check[j - min_val] = False

    return sum(check)

min_val, max_val = list(map(int, input().split()))
print(solution(min_val, max_val))


