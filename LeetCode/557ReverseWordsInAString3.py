#https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        print(s)
        for i in range(len(s)):
            s[i]=s[i][::-1]
        print(s)
        return " ".join(s)