#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([st for st in s.split(" ") if st!=""][::-1])