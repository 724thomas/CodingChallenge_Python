#https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

class Solution:
    def minTimeToType(self, word: str) -> int:
        place=1
        ans=0
        fst = "a"
        for i in range(len(word)):
            a=( abs(idx(fst)-idx(word[i])) )
            b=(26 - ( max(idx(fst),idx(word[i])) - min(idx(fst),idx(word[i]))))
            ans+=min(a,b)+1
            fst=word[i]
        return ans
def idx(char):
    return ord(char)-96