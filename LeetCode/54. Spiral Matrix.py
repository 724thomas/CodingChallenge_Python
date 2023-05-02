#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top=0
        bottom=len(matrix)-1
        left=0
        rightlen(matrix[0])-1
        direction = 0

        while top <= bottom and left <= right:
            if direction == 0:
                for i in range(left, right+1):
                    result.append(matrix[top][i])
                top += 1
            elif direction == 1:
                for i in range(top, bottom+1):
                    result.append(matrix[i][right])
                right -= 1
            elif direction == 2:
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            elif direction == 3:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
            direction = (direction+1) % 4

        return result
