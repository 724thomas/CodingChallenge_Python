#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        snum2 = Counter(nums2)

        for num in nums1:
            if snum2[num]!=0:
                ans.append(num)
                snum2[num]-=1
        return ans
