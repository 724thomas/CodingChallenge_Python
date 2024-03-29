# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/

'''
1. 아이디어 :
    1. 해시셋으로 각 숫자의 합을 구한후, 정렬하여 반환하면 된다.
    2. 두 배열의 첫번째 원소를 비교하여, 작은것을 결과에 추가하고, 해당 배열의 첫번째 원소를 제거한 후, 결과값에 남은 배열을 합친다.
2. 시간복잡도 :
    1. O(nLogn) : n은 해시셋으로 만드는 과정, nlogn은 정렬하는 과정
    2. O(n) : n은 nums의 길이
3. 자료구조 :
    1. 해시셋
    2. 리스트
'''


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums = {}
        for n in nums1:
            if n[0] not in nums:
                nums[n[0]]=n[1]
            else:
                nums[n[0]]+=n[1]
        for n in nums2:
            if n[0] not in nums:
                nums[n[0]]=n[1]
            else:
                nums[n[0]]+=n[1]

        return sorted([k,v] for k,v in nums.items())


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []

        while nums1 and nums2:

            if nums1[0][0] == nums2[0][0]:
                ans.append([nums1[0][0],nums1[0][1]+nums2[0][1]])
                nums1.pop(0)
                nums2.pop(0)
            elif nums1[0][0] < nums2[0][0]:
                ans.append([nums1[0][0],nums1[0][1]])
                nums1.pop(0)
            else:
                ans.append([nums2[0][0],nums2[0][1]])
                nums2.pop(0)

        return ans +nums1+nums2