#https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters={}
        for char in s:
            if char not in letters:
                letters[char]=1
            else:
                letters[char]+=1

        result=0
        isodd=False
        for i in letters.values():
            if i >1:
                if i%2==0:
                    result+=i
                else:
                    result+=i-1
                    isodd=True
            else:
                isodd=True
        if isodd==True:
            result+=1
        return result
