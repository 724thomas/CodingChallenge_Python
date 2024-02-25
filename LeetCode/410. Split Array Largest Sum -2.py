#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def is_possible(n):
            curr = 0
            count = 0
            for num in nums:
                if curr + num <= n:
                    curr += num
                else:
                    curr = num
                    count += 1
                if count > k:
                    return False
            if curr:
                count+=1

            return False if count>k else True


        left = max(nums)
        right = sum(nums)-1
        while left<=right:
            mid = (left+right)//2
            if is_possible(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left