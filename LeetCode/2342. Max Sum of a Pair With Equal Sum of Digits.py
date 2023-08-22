#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        def sdigit(n):
            total=0
            s=str(n)
            for i in range(len(s)):
                total+=int(s[i])
            return total


        nmap={}
        for n in nums:
            d=sdigit(n)
            if d not in nmap:
                nmap[d]=[]
            nmap[d].append(n)
        cmax=-1
        for k,v in nmap.items():
            if len(v)>=2:
                nmap[k]=sorted(v)
                cmax=max(cmax, nmap[k][-1]+nmap[k][-2])

        return cmax

