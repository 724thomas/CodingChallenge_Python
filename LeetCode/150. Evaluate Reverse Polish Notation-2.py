#

'''
1. 아이디어 :
    스택을 사용
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    스택
'''


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))

            else:
                if t == "+":
                    stack.append(stack.pop() + stack.pop())
                elif t == "-":
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(left-right)
                elif t == "*":
                    stack.append(stack.pop() * stack.pop())
                else:
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(int(left/right))

        return stack[0]