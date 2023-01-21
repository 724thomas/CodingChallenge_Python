# https://leetcode.com/problems/minimize-product-sum-of-two-arrays/description/

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1=sorted(nums1, reverse=True)
        nums2.sort()
        ans=0
        for i in range(len(nums1)):
            ans+=nums1[i]*nums2[i]
        return ans
