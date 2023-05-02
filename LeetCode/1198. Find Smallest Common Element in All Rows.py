#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        ans=set(mat[0])
        for i in range(1,len(mat)):
            ans=ans& set(mat[i])

        return min(ans) if len(ans)>=1 else -1