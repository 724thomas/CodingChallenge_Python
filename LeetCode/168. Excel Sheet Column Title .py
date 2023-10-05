# https://leetcode.com/problems/excel-sheet-column-title/description/

'''
1. 아이디어 :
    26으로 나눈 몫을 계속 더해주면 된다
2. 시간복잡도 :
    O(1)
3. 자료구조 :
    배열
'''

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        capitals = [chr(64 + i) for i in range(1, 27)]
        ans = ""
        while columnNumber > 0:
            ans = capitals[(columnNumber-1)%26] + ans
            columnNumber = (columnNumber-1) // 26
        return ans