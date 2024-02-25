#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]: # 0번째가 답일때
            return nums[0]
        if nums[0] > nums[1]: # 1번째가 답일때
            return nums[1]
        if nums[-2] > nums[-1] < nums[0]: #마지막이 답일때
            return nums[-1]
        if nums[-3] > nums[-2] < nums[-1]: #마지막-1이 답일때
            return nums[-2]

        left = 0
        right = len(nums)-1

        while left<=right:
            mid = (left+right)//2
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[0] < nums[mid] > nums[-1]:
                left = mid + 1
            elif nums[0] > nums[mid] < nums[-1]:
                right = mid - 1
