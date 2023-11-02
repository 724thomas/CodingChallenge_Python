#https://leetcode.com/problems/find-the-difference-of-two-arrays/description/

'''
1. 아이디어 :
    해시셋으로 만들어서 확인한다.
2. 시간복잡도 :
    O(2n)
3. 자료구조 :
    해시셋
'''

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = [[],[]]
        nums1 = set(nums1)
        nums2 = set(nums2)

        for n in nums1:
            if n not in nums2:
                ans[0].append(n)
        for n in nums2:
            if n not in nums1:
                ans[1].append(n)

        return ans