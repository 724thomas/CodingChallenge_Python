# https://leetcode.com/problems/move-zeroes/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        write_idx, move_idx = 0, 0

        while move_idx < len(nums):
            if nums[move_idx] != 0:
                nums[write_idx], nums[move_idx] = nums[move_idx], 0
                write_idx += 1
            move_idx +=1
