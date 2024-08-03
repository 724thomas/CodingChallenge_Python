#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for j in range(len(matrix)//2):
            for i in range(len(matrix)-1-(2*j)):
                matrix[0+j][i+j], matrix[i+j][-1-j], matrix[-1-j][-1-i-j], matrix[-1-i-j][j] = matrix[-1-i-j][j], matrix[j][i+j], matrix[i+j][-1-j], matrix[-1-j][-1-i-j]