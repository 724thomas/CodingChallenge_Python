# https://leetcode.com/problems/plus-one/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remain = True
        for i in range(len(digits)-1,-1,-1):
            if remain:
                digits[i] += 1
                if digits[i] == 10:
                    digits[i] = 0
                    remain = True
                else:
                    remain = False
        return [1] + digits if remain else digits