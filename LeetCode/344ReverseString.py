#https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        leng=len(s)
        for i in range(int(len(s)/2)):
            s[i],s[-1-i]=s[-1-i],s[i]

                