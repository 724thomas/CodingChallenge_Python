#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def groupThePeople(self, g: List[int]) -> List[List[int]]:
        ans=[]
        for i in range(1,len(g)+1):
            temp=[]
            for j in range(len(g)):
                if g[j]==i:
                    temp.append(j)
                if len(temp)==i:
                    ans.append(temp.copy())
                    temp=[]
        return ans