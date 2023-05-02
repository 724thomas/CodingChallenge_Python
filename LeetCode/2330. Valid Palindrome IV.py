#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def makePalindrome(self, s: str) -> bool:
        count=0
        st=0
        en=len(s)-1
        for i in range(len(s)//2):
            if s[st]!=s[en]:
                count+=1
                if count>2:
                    return False
            st+=1
            en-=1
        return True