#https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        ans=""
        count=0
        for i in str(num):
            if i=="9":
                ans+="9"
            elif i=="6" and count==0:
                ans+="9"
                count+=1
            else:
                ans+="6"
        return int(ans)