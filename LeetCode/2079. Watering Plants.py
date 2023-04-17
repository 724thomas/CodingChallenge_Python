#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def wateringPlants(self, plants: List[int], c: int) -> int:
        p=[0]+plants
        ans=0
        cmax=c
        for i in range(1,len(p)):
            if c>=p[i]:
                c-=p[i]
                ans+=1
            elif c<p[i]:
                ans+=(2*i)-1
                c=cmax-p[i]
        return ans


