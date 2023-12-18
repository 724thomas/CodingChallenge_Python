# https://leetcode.com/problems/rotate-array/description/

'''
1. 아이디어 :
    - nums[-(k % len(nums)):] : 오른쪽에서 k번째까지
    - nums[:-(k % len(nums))] : 나머지
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    배열
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]