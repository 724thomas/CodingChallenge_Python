#https://leetcode.com/problems/reverse-only-letters/description/

class Solution(object):
    def reverseOnlyLetters(self, S):
        letters = [c for c in S if c.isalpha()]
        ans = []
        for char in S:
            if char.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(char)
        return "".join(ans)