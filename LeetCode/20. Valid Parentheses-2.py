#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for c in s:
            if c in dic:
                stack.append(dic[c])
            elif not stack or stack.pop() != c:
                return False

        return not stack