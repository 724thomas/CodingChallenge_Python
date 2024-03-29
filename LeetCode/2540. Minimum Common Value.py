# https://leetcode.com/problems/minimum-common-value/

'''
1. 아이디어 :
     for문을 돌면서 nums1의 원소를 target으로 잡고, nums2에서 이진탐색으로 찾는다.
2. 시간복잡도 :
    O(N * logN)
    num1 길이 * 이분탐색 logN
3. 자료구조 :
    배열
'''

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        for target in nums1:
            start = 0
            end = len(nums2) - 1
            while start<=end:
                mid = (start+end)//2
                if nums2[mid] == target:
                    return nums2[mid]
                elif nums2[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1


        return -1