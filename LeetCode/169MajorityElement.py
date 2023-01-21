#https://leetcode.com/problems/majority-element/description/

import statistics
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return statistics.mode(nums)