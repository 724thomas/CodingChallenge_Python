#https://leetcode.com/problems/largest-subarray-length-k/

class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        nindex,nmax=0,0
        for i in range(len(nums)-k+1):
            if nums[i]>nmax:
                nmax=nums[i]
                nindex=i
        return (nums[nindex:nindex+k])