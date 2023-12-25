# https://leetcode.com/problems/plus-one/description/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return ([int(x) for x in str(int("".join([str(x) for x in digits]))+1)])