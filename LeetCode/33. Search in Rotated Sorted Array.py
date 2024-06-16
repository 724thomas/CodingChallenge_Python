#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            if nums[mid] >= nums[left]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid-1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and target <=nums[right]:
                    left = mid+1
                else:
                    right = mid -1

        return -1