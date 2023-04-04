#https://leetcode.com/problems/majority-element-ii/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=[]
        times=int(len(nums)/3)
        c=Counter(nums)
        for k,v in c.items():
            if v>times:
                ans.append(k)
        return ans