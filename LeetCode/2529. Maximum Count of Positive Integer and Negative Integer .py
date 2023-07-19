# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

'''
1. 아이디어 :
    1) 이분탐색
2. 시간복잡도 :
    1) O(logn)
3. 자료구조 :
    1) 배열
'''



class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if nums[0]>0 or nums[-1]<0:
            return len(nums)

        left = 0
        right = len(nums)-1

        while left<=right:
            mid = (left+right)//2

            if nums[mid] >= 0:
                right = mid - 1
            else:
                left = mid + 1
        neg = left


        left = 0
        right = len(nums)-1

        while left<=right:
            mid = (left+right)//2

            if nums[mid] >= 1:
                right = mid - 1
            else:
                left = mid + 1

        pos = len(nums) - left
        return max(neg,pos)