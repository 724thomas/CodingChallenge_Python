#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for b in s:
            if b==")":
                if len(stack)==0 or stack[-1] !="(":
                    stack.append(b)
                else:
                    stack.pop()
            else:
                stack.append(b)
        return len(stack)