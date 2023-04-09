# https://leetcode.com/problems/minimum-common-value/description/

'''
1. 아이디어 :
    1) 정렬된 배열이므로, 두 배열의 첫번째 원소부터 비교하면서 같은 원소가 나오면 리턴
    2) 길이 작은 배열을 num1으로 두고, 이분탐색을 통해 num1의 원소가 num2에 있는지 확인
2. 시간복잡도 :
    1) O(N+M)
    2) O(NlogM)
3. 자료구조 :
    1) 배열
    2) 배열
'''

#1)
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        idx1 = 0
        idx2 = 0
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] == nums2[idx2]:
                return nums1[idx1]
            elif nums1[idx1] < nums2[idx2]:
                idx1+=1
            else:
                idx2+=1
        return -1

#2)
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