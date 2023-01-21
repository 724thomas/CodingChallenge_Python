# https://leetcode.com/problems/move-zeroes/description/
'''
1. 아이디어 :
    1) 투 포인터로, 제일 첫번째 0에 index를 두고, 0이 아닐경우 0으로 바꾸고, 0이면 index를 늘린다.
2. 시간복잡도 :
    1) O(n)
    - for문을 돌면서 조건문 확인
3. 자료구조 :
    1) 배열
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        for j in range(len(nums)):
            if(nums[i]==0 and nums[j]!=0):
                nums[i],nums[j]=nums[j],nums[i]
            if(nums[i]!=0):
                i+=1
        





