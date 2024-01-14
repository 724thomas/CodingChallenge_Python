# https://leetcode.com/problems/generate-parentheses/description/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left = [0]
        right = [0]

        ans = []
        temp = []

        def backtrack(left, right):
            if left > n or right > n or right>left:
                return

            if len(temp) == n*2:
                ans.append("".join(temp))
                return

            temp.append("(")
            backtrack(left+1, right)
            temp.pop()
            temp.append(")")
            backtrack(left, right+1)
            temp.pop()

        backtrack(0, 0)
        return ans