#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1

        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1

            elif nums[mid] < target:
                left = mid + 1

        return left