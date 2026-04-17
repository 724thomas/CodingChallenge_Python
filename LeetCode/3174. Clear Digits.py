#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import deque

class Solution:
    def clearDigits(self, s: str) -> str:
        chars = deque()
        for char in s:
            if (char.isalpha()):
                chars.append(char)
            else:
                chars.pop()
        return "".join(chars)