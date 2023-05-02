#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dc={}

        while cpdomains:
            s=cpdomains.pop().split(" ")
            count=int(s[0])
            d=s[1].split(".")

            for i in range(len(d)):
                sd=".".join(d[i:])
                if sd not in dc:
                    dc[sd]=count
                else:
                    dc[sd]+=count

        ans=[]
        for k,v in dc.items():
            ans.append(str(v) + " " + k)
        return ans