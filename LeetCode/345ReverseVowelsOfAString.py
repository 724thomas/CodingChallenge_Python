#https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        c={}
        v='aeiouAEIOU'
        ans=""
        for i in range(len(s)):
            if s[i] in v:
                c[i]=s[i]
        for i in s:
            if i in v:
                cmax=max(c)
                ans+= c[cmax]
                del c[cmax]
            else:
                ans+=i
        return ans