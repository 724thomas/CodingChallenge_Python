#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = [nums[0]]
        for i in range(1, len(nums)):
            for j in range(len(stack)):
                if nums[i] <= stack[j]:
                    stack[j] = nums[i]
                    break
            else:
                stack.append(nums[i])

        return len(stack)