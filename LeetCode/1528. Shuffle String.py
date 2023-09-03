#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans=[""]*len(indices)
        for i in range(len(indices)):
            ans[indices[i]]=s[i]
        return "".join(ans)