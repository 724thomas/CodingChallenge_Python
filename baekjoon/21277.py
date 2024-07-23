# https://www.acmicpc.net/problem/21277

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()


def solution(r1, c1, puzzle1, r2, c2, puzzle2):
    def rotate_cw(arr):
        ans = []
        for col in range(len(arr[0])):
            temp = []
            for row in range(len(arr) - 1, -1, -1):
                temp.append(arr[row][col])
            ans.append(temp)
        return ans

    def placeable(row, col, puzzle2):
        for i in range(len(puzzle2)):
            for j in range(len(puzzle2[0])):
                #puzzle1 범위 채크
                if 0 <= row + i < r1 and 0 <= col + j < c1 and puzzle1[row + i][col + j] == "1" and puzzle2[i][j] == "1":
                    return False
        return True

    def calc_area(row, col, puzzle2):
        max_row = max(r1, row + len(puzzle2)) - min(0, row)
        max_col = max(c1, col + len(puzzle2[0])) - min(0, col)
        # 퍼즐2가 왼쪽/위쪽에 있을때 -min
        return max_col * max_row

    rotated_puzzle2 = [puzzle2]
    for i in range(3):
        rotated_puzzle2.append(rotate_cw(rotated_puzzle2[-1]))

    ans = float('inf')
    for row in range(-r2, r1+r2):
        for col in range(-c2, c1+c2):
            for puzzle2 in rotated_puzzle2:
                if placeable(row, col, puzzle2):
                    ans = min(ans, calc_area(row, col, puzzle2))

    return ans


if __name__ == '__main__':
    r1, c1 = list(map(int, input().strip().split()))
    puzzle1 = list(list(map(str, input().strip())) for _ in range(r1))
    r2, c2 = list(map(int, input().strip().split()))
    puzzle2 = list(list(map(str, input().strip())) for _ in range(r2))
    print(solution(r1, c1, puzzle1, r2, c2, puzzle2))
