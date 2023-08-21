#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        nmap={}
        nset=set()
        count=0
        cmax=0
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
            else:
                if count not in nmap:
                    nmap[count]=1
                else:
                    nmap[count]+=1
                nset.add(count)
                cmax=max(cmax,count)
                count=0
        nset.add(count)
        if count not in nmap:
            nmap[count]=1
        else:
            nmap[count]+=1
        cmax=max(cmax, count)
        ans=0
        dp=[0]*(cmax+1)
        for i in range(1,len(dp)):
            dp[i]=dp[i-1]+i
        for k,v in nmap.items():
            ans+=v*dp[k]
        return ans
