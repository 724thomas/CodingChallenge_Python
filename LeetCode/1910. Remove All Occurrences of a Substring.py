#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s=s.replace(part,"",1)
        return s