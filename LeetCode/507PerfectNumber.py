#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        temp=0
        for i in range(1,int(num**0.5)+1):
            if num/i==int(num/i):
                temp+=i
                temp+=num/i
        return temp-num==num
