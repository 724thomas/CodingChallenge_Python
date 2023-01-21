#https://leetcode.com/problems/wiggle-sort/

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:

        nums.sort()
        hp=[]
        left=0
        right=len(nums)-1
        while left<right:
            hp.append(nums[left])
            hp.append(nums[right])
            left+=1
            right-=1
        if len(hp)!=len(nums):
            hp.append(nums[ int(len(nums)/2-0.5)  ])
        print(hp)
        for i in range(len(hp)):
            nums[i]=hp[i]


        """
        Do not return anything, modify nums in-place instead.
        """
