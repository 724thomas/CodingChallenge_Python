# https://leetcode.com/problems/next-greater-element-i/description/

'''
1. 아이디어 :
    monotonic stack
2. 시간복잡도 :
    O( n )
3. 자료구조 :

'''

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = { n:i for i, n in enumerate(nums1)}
        print(nums1Idx)
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur
            if cur in nums1Idx:
                stack.append(cur)

        return res
