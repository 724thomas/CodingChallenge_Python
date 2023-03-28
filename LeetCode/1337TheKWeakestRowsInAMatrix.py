#https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans=[]
        for i in range(len(mat)):
            ans.append([sum(mat[i]),i])
        ans.sort()
        return [ans[i][1] for i in range(k)]