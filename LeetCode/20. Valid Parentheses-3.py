#

'''
1. 아이디어 :
    스택을 사용한다
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    스택
'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in "({[":
                stack.append(c)
            elif c in map.keys():
                if stack and stack[-1] == map[c]:
                    stack.pop()
                else:
                    return False

        return False if stack else True