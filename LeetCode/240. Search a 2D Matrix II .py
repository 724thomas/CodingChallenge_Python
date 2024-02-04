# https://leetcode.com/problems/search-a-2d-matrix-ii/description/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        for row in range(ROWS):

            l, r = 0, COLS - 1
            while l <= r:
                m = (l + r) // 2
                if target > matrix[row][m]:
                    l = m + 1
                elif target < matrix[row][m]:
                    r = m - 1
                else:
                    return True
        return False