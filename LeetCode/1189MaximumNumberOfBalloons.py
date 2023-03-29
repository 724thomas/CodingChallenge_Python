#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s1="balloon"
        chars={}
        for c in text:
            if c not in chars:
                chars[c]=1
            else:
                chars[c]+=1

        if "l" in chars:
            chars["l"]=int(chars["l"]/2)
        if "o" in chars:
            chars["o"]=int(chars["o"]/2)

        ans=float("inf")
        for s in s1:
            if s not in chars:
                return 0
            else:
                ans=min(ans, chars[s])
        return ans