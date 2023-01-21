#https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        if number.count(digit)==1:
            return number[:number.index(digit)] + number[number.index(digit)+1:]
        number+="0"
        for i in range(len(number)-1):
            if number[i]==digit:
                index=i
                if number[i+1]>number[i]:
                    return number[:i] + number[i+1:-1]
        return number[:index] + number[index+1:-1]