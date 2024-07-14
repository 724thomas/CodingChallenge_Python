#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ")":
                stack.append(c[::-1])
            else:
                temp = []
                while stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                stack += temp.copy()
        return "".join(stack)