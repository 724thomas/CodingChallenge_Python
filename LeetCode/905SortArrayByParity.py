#https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        elist=[]
        olist=[]
        for i in nums:
            if i%2==0:
                elist.append(i)
            else:
                olist.append(i)
        return elist+olist