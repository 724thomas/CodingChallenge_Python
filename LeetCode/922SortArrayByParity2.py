#https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        no=1
        ne=0
        alist=[0]*len(nums)
        print(alist)

        for i in nums:
            if i%2==0:
                alist[ne]=i
                ne+=2
            else:
                alist[no]=i
                no+=2
        return alist