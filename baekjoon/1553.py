# https://www.acmicpc.net/problem/1553

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(arr):
    for a in arr:
        print(a)
    check = [[False] * 7 for _ in range(8)]
    dominos = [[False] * 7 for _ in range(7)]
    ans = [0]

    def backtrack(row, col):
        if row == 8:
            ans[0] += 1
            return
        if col == 7:
            backtrack(row + 1, 0)
            return

        if check[row][col]:
            backtrack(row, col + 1)
            return

        curr = arr[row][col]
        check[row][col] = True
        for row2, col2 in ((0, 1), (1, 0)):
            nrow, ncol = row + row2, col + col2
            if 0 <= nrow < 8 and 0 <= ncol < 7:
                pair = arr[nrow][ncol]

                if not check[nrow][ncol] and not dominos[curr][pair]:
                    dominos[curr][pair] = dominos[pair][curr] = True
                    check[nrow][ncol] = True

                    backtrack(row, col + 1)

                    check[nrow][ncol] = False
                    dominos[curr][pair] = dominos[pair][curr] = False

        check[row][col] = False

    backtrack(0, 0)
    return ans[0]


arr = []
for _ in range(8):
    s = str(input().strip())
    temp = []
    for c in s:
        temp.append(int(c))
    arr.append(temp)
print(solution(arr))
