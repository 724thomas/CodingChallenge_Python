# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

'''
1. 아이디어 :
    범위를 구해서, 해시셋에 있는지 확인한다
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    해시셋
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        nums = set(nums)
        ans = []

        for i in range(1,length+1):
            if i not in nums:
                ans.append(i)
        return ans
