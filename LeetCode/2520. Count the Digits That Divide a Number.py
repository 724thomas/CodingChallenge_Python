#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        c=str(num)
        for n in c:
            if num%int(n)==0:
                count+=1
        return count