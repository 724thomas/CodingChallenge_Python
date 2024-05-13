#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                right = stack.pop()
                left = stack.pop()
                if t == "+":
                    stack.append(left+right)
                elif t == "-":
                    stack.append(left-right)
                elif t == "*":
                    stack.append(left*right)
                elif t == "/":
                    stack.append(int(left/right))
        return stack[-1]
