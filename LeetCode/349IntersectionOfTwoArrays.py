# https://leetcode.com/problems/intersection-of-two-arrays/
'''
1. 아이디어 :
    1) set으로 중복을 제거한 후, 두개의 set을 비교하여 교집합을 구한다.
2. 시간복잡도 :
    1) O(n)
3. 자료구조 :
    1) Set

'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
