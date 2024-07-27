#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for n in nums:
            pos = bisect_left(stack, n)
            if pos == len(stack):
                stack.append(n)
            else:
                stack[pos] = n
        return len(stack)