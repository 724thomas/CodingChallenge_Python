#

'''
1. 아이디어 :
    이분탐색을 두번한다
2. 시간복잡도 :
    O( nlogn)
3. 자료구조 :
    이분탐색
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        left = 0
        right = len(matrix)-1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1

        row = matrix[right]


        left = 0
        right = len(row)-1

        while left <= right:
            mid = (left + right) // 2

            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False