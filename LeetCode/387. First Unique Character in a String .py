# https://leetcode.com/problems/first-unique-character-in-a-string/description/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        c=Counter(s)
        for i in range(len(s)):
            if c[s[i]]==1:
                return i
        return -1