# https://leetcode.com/problems/contains-duplicate/description/

'''
1. 아이디어 :
    해시셋 사용
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    해시셋
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))