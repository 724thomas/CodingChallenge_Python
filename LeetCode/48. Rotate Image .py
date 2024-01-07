# https://leetcode.com/problems/rotate-image/description/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        length = len(matrix)
        for j in range(length//2):
            for i in range(length-(j*2)-1):
                matrix[0+j][i+j], matrix[i+j][-1-j], matrix[-1-j][-1-i-j], matrix[-1-i-j][0+j] = matrix[-1-i-j][0+j], matrix[0+j][i+j], matrix[i+j][-1-j], matrix[-1-j][-1-i-j]