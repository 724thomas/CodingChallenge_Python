# https://leetcode.com/problems/basic-calculator-ii/description/

'''
1. 아이디어 :
    스택을 사용한다.
    s의 " "를 제거하고, "+"를 추가해서 마지지막 num까지 처리할 수 있도록 한다.
    +, -를 만나면 숫자를 스택에 넣고
    *, /를 만나면 숫자를 스택에서 꺼내서 계산한 후 다시 스택에 넣는다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    스택
'''

class Solution:
    def calculate(self, s: str) -> int:
        s=s.replace(" ","") + "+"
        operation = "+"
        stack = []
        num = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)

            elif not c.isdigit():
                if operation == "+":
                    stack.append(num)
                elif operation == "-":
                    stack.append(-num)
                elif operation == "*":
                    prev = stack.pop()
                    stack.append(prev * num)
                elif operation == "/":
                    prev = stack.pop()
                    stack.append(math.trunc(prev/num))

                num=0
                operation = c

        return sum(stack)