#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        def dfs(t):
            if len(t)==1:
                return t[0]
            temp=[]
            for i in range(len(t)-1):
                temp.append(t[i]+t[i+1])
            return dfs(temp)
        return dfs(nums) % 10