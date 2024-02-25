# https://leetcode.com/problems/search-a-2d-matrix/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][0] < target:
                left = mid + 1

        matrix = matrix[right]

        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid] == target:
                return True
            elif matrix[mid] > target:
                right = mid - 1
            elif matrix[mid] < target:
                left = mid + 1

        return False
