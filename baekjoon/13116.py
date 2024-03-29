# https://www.acmicpc.net/problem/13116

'''
1. 아이디어 :
    1) 두 수를 비교하면서, 더 큰 수를 반으로 나누면서 비교한다.
2. 시간복잡도 :
    1)  O(n) * O(logn) = O(nlogn)
    -   테스트 케이스 * while문
3. 자료구조 :
    1)  X
'''


import sys
input = sys.stdin.readline
for i in range(int(input())):
    a, b = map(int, input().split())
    while a!=b:
        if a > b:
            a = a // 2
        else:
            b = b // 2
    print(a*10)

