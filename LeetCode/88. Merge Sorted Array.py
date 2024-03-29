# https://leetcode.com/problems/merge-sorted-array/description/

'''
1. 아이디어 :
    m+n만큼 뒤에서부터 하나씩 채워나가고, 두 배열중 큰값을 채워나가면 된다.
2. 시간복잡도 :
    O(m+n) : m은 nums1의 길이, n은 nums2의 길이
3. 자료구조 :
    리스트
'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1 = m-1
        idx2 = n-1
        write_idx = m+n-1

        while idx2 >=0:
            if idx1>=0 and nums1[idx1] > nums2[idx2]:
                nums1[write_idx] = nums1[idx1]
                idx1-=1
            else:
                nums1[write_idx] = nums2[idx2]
                idx2-=1
            write_idx-=1