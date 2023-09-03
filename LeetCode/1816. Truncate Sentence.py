#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split(" ")[:k])