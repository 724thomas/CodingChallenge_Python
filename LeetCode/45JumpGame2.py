#https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        res=0
        l,r=0,0

        far=1
        while r<len(nums)-1:
            for i in range(l,r+1):
                if far<i+nums[i]:
                    far=i+nums[i]
            l=r+1
            r=far
            res+=1

        return res
