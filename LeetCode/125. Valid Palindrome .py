# https://leetcode.com/problems/valid-palindrome/description/

'''
1. 아이디어 :

2. 시간복잡도 :
    O( n )
3. 자료구조 :

'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        check = ""
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz0123456789":
                check += c
        return check == check[::-1]
