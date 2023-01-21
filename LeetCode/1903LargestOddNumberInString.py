#https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        num=num[::-1]
        for i in range(len((num))):
            if int(num[i])%2==1:
                return num[i::][::-1]
        return ""