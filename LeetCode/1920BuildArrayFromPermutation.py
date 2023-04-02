#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans