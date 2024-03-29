#https://leetcode.com/problems/plus-one/

'''
1. 아이디어 :
    숫자를 String으로 변환후 합치고, 1을 더한후 다시 숫자로 변환후 리스트로 변환하여 반환.
2. 시간복잡도 :
    O(n) : n은 digits의 길이
3. 자료구조 :
    리스트
'''


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return ([int(x) for x in str(int("".join([str(x) for x in digits]))+1)])