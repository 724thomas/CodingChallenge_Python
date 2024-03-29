# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid

            if nums[mid] >= nums[l]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid-1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <=nums[r]:
                    l = mid+1
                else:
                    r = mid -1

        return -1
