#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def removeVowels(self, s: str) -> str:
        ans=""
        for c in s:
            if c not in "aeiou":
                ans+=c
        return ans