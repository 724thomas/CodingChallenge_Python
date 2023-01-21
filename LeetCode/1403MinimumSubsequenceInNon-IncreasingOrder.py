#https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums=sorted(nums)[::-1]
        total=sum(nums)
        adding=0
        ans=[]
        for num in nums:
            if adding<=total:
                ans.append(num)
                adding+=num
                total-=num
        return ans