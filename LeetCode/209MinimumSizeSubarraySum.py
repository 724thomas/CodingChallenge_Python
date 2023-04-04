#https://leetcode.com/problems/minimum-size-subarray-sum/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=len(nums)+1
        total=left=right=0
        for i in range(len(nums)):
            total+=nums[right]
            while total>=target:
                ans=min(ans, right-left+1)
                total-=nums[left]
                left+=1
            right+=1

        return ans if sum(nums)>=target else 0