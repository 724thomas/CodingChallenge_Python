#https://leetcode.com/problems/set-matrix-zeroes/description/

'''
1. 아이디어 :
    0이 포함된 row, col을 모두 저장하고, 저장된 row, col 값을 0으로 변경한다.
2. 시간복잡도 :
    O(n^2)
3. 자료구조 :
    배열
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (matrix[row][col] == 0):
                    rows.add(row)
                    cols.add(col)
        for row in rows:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0
        for col in cols:
            for row in range(len(matrix)):
                matrix[row][col] = 0
        return