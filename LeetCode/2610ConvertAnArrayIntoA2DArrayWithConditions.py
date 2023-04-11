#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        c=Counter(nums)
        cmax=0
        for num in nums:
            cmax=max(cmax, nums.count(num))
        ans=[]

        for i in range(cmax):
            temp=[]
            for k,v in c.items():
                if v!=0:
                    temp.append(k)
                    c[k]-=1
            ans.append(temp.copy())
        return ans
