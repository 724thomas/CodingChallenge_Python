#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(0,len(nums),2):
            freq=nums[i]
            val=nums[i+1]
            for i in range(freq):
                ans.append(val)
        return ans
