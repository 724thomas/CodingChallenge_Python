#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        while num:
            if num%2==0:
                num=num//2
            else:
                num=num-1
            count+=1
        return count
