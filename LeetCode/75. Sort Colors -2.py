# https://leetcode.com/problems/sort-colors/description/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1, p2, p3 = 0, 0, len(nums) - 1

        while p1 <= p3:
            if nums[p1] == 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 += 1
                p1 += 1
            elif nums[p1] == 2:
                nums[p1], nums[p3] = nums[p3], nums[p1]
                p3 -= 1
            else:
                p1 += 1