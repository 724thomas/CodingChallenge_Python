#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        lp=0
        rp=0
        longest=""
        clongest=""
        while rp<len(s):
            if s[rp] not in clongest:
                clongest+=s[rp]
                rp+=1
            else:
                if len(longest)<len(clongest):
                    longest=clongest
                clongest = clongest[clongest.index(s[rp])+1:]
        return max(len(longest),len(clongest))

