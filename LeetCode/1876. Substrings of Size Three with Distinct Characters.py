#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        def isvalid(str):
            return False if str[0]==str[1] or str[1] == str[2] or str[0]==str[2] else True

        if len(s)<3:
            return 0
        count=0
        for i in range(len(s)-2):
            count+=isvalid(s[i:i+3])
        return count



