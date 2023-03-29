#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        print(nums)
        ans=0
        count=1
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                ans=max(ans,count)
                count=1
            else:
                count+=1
        ans=max(ans,count)
        return ans

