#https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def checkInAllStrings(string, place, strList):
            for i in strList:
                try:
                    if i[place]!=string:
                        return False
                except:
                    return False
            return True

        ans=""
        for i in range(len(strs[0])):
            if checkInAllStrings(strs[0][i],i,strs[1:]):
                ans+=(strs[0][i])
            else:
                return ans
        return ans