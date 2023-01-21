#https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        adict={5:0,10:0,20:0}
        for i in bills:
            adict[i]+=1
            if i==10:
                if adict[5]==0:
                    return False
                adict[5]-=1
            if i==20:
                if adict[10]==0:
                    if adict[5]>=3:
                        adict[5]-=3
                    else:
                        return False
                else:
                    adict[10]-=1
                    if adict[5]>=1:
                        adict[5]-=1
                    else:
                        return False
        return True