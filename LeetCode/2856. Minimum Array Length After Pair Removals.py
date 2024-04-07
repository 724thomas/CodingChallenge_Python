#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        length = len(nums)
        left = 0
        mid = (length+1)//2
        ans=length

        while left < length//2 and mid < length:
            if nums[left] < nums[mid]:
                ans -= 2
            left += 1
            mid += 1

        return ans
