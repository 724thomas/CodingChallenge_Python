#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        cmax = 0
        ans = ""
        for i in range(len(s)):

            l,r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1) > cmax:
                    cmax = (r-l+1)
                    ans = s[l:r+1]
                l-=1
                r+=1

            l,r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1) > cmax:
                    cmax = (r-l+1)
                    ans = s[l:r+1]
                l-=1
                r+=1

        return ans