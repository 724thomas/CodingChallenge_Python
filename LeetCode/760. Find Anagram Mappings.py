#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nidx={nums2[i]:i for i in range(len(nums2))}
        for i in range(len(nums1)):
            nums1[i]=nidx[nums1[i]]
        return nums1