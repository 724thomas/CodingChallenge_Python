#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        ans = [[1]]
        for i in range(n-1):
            last = ans[-1]
            temp = [1]
            for j in range(i):
                temp.append(last[j]+last[j+1])
            temp.append(1)
            ans.append(temp)
        return ans
