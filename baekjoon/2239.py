# https://www.acmicpc.net/problem/2239

'''
1. 아이디어 :
    백트래킹으로 풀면된다.
2. 시간복잡도 :
    O(9!)
3. 자료구조 :
    해시셋
'''


import sys
input = sys.stdin.readline

board = []
for i in range(9):
    nums = input().rstrip()
    temp=[int(num) for num in nums]
    board.append(temp)

for row in board:
    print(row)


