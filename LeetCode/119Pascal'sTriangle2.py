#https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[1]
        for i in range(rowIndex):
            temp=[0]+res+[0]
            tlist=[]
            for j in range(len(res)+1):
                tlist.append(temp[j]+temp[j+1])
            res=tlist
        return res