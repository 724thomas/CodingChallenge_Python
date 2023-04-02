#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        def fac(n):
            ans=0
            while n!=0:
                n-=1
                ans+=n
            return ans

        c=Counter(nums)
        ans=0
        for k,v in c.items():
            if v>=2:
                ans+=(fac(v))
        return ans
