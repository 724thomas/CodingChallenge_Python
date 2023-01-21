#https://leetcode.com/problems/reverse-string-ii/

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        start=0
        end=0
        i=0
        ans=""
        while end<len(s):
            start=(2*k*i)
            end=(2*k*i+k)
            next=(2*k*(i+1))
            print(s[start:end])
            i+=1
            ans+=s[start:end][::-1]
            ans+=s[end:next]
        return ans
