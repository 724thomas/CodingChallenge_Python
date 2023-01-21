#https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=max(len(word1),len(word2))
        print(l)
        ans=""
        for i in range(l):
            try:
                ans+=word1[i]
            except:
                pass
            try:
                ans+=word2[i]
            except:
                pass
        print(ans)
        return ans