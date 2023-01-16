# https://leetcode.com/problems/search-a-2d-matrix-ii/description/

'''
1. 아이디어 :
    1) 정렬된 배열로, 이분탐색을 한다.
2. 시간복잡도 :
    1) (n) * (logn) = O(nlogn)
    - 행 * 행마다 이분탐색
3. 자료구조 :
    1) 2차원 배열
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            start=0
            end=len(nums)-1
            while start<=end:
                mid = (start+end)//2
                if nums[mid]==target:
                    return True
                elif nums[mid]<target:
                    start = mid+1
                elif nums[mid]>target:
                    end = mid -1
        return False