#https://leetcode.com/problems/strobogrammatic-number/description/

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        lp=0
        rp=len(num)-1
        while lp<=rp:
            if num[lp] not in "01869":
                return False
            if num[lp] in "018":
                if num[lp]!=num[rp]:
                    return False
            if num[lp] == "6":
                if num[rp]!="9":
                    return False
            if num[lp] == "9":
                if num[rp]!="6":
                    return False
            lp+=1
            rp-=1
        return True