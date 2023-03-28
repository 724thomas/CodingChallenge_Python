#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if len(s)<=1:
            return True

        isodd=len(s)%2
        c={}
        for char in s:
            if char not in c:
                c[char]=1
            else:
                c[char]+=1
        if len(c)<=1:
            return True

        if isodd:
            count=0
            for k,v in c.items():
                if v%2==1:
                    count+=1
            return count==1
        else:
            for k,v in c.items():
                if v%2==1:
                    return False
        return True