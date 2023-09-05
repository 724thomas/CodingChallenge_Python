# https://leetcode.com/problems/generate-parentheses/

'''
1. 아이디어 :
    백트래킹을 사용. left를 먼저 채우고, right를 채워나가는 방식
2. 시간복잡도 :
    O(2^n)
3. 자료구조 :
    배열
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.left = self.right = n
        ans = []
        def bt(s):

            if not self.left and not self.right:
                ans.append(s)

            if self.left:
                self.left-=1
                bt(s+"(")
                self.left+=1

            if self.right>self.left:
                self.right-=1
                bt(s+")")
                self.right+=1

        bt("")
        return ans