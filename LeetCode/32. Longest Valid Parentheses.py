#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        cmax = 0
        stack=[-1]

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    cmax=max(cmax, i-stack[-1])

        return cmax