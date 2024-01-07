# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

'''
1. 아이디어 :
    이분탐색을 두번한다.
    첫번째는 첫 인덱스를 구하기 위해, nums[mid] < target으로, left
    두번쨰는 끝 인덱스를 구하기 위해, nums[mid] <= target으로 right-1
2. 시간복잡도 :
    O(nlogn)
3. 자료구조 :
    배열
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums_set = set(nums)
        if target not in nums_set:
            return [-1,-1]

        ans = []
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid - 1
        ans.append(left)

        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] <= target:
                left = mid+1
            else:
                right = mid - 1
        ans.append(left-1)
        return ans