#https://leetcode.com/problems/number-of-arithmetic-triplets/

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans=0
        for i in range(len(nums)-2):
            base=nums[i]
            count=0
            for j in range(i+1,len(nums)):
                if nums[j]-base ==diff:
                    count+=1
                    base=nums[j]
                elif nums[j]-base>diff:
                    break
                if count==2:
                    ans+=1
                    break
        print(ans)
        return ans