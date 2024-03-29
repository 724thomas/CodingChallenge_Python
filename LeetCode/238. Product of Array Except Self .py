# https://leetcode.com/problems/product-of-array-except-self/

'''
1. 아이디어 :
    0이 2개 이상이면 0으로 가득찬 리스트를 리턴
    0이 1개면 0이 아닌 수들의 곱을 0의 위치에 넣어준다.
    0이 없으면 전체 곱을 각각의 수로 나눠준다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    배열
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = [i for i, num in enumerate(nums) if num == 0]
        ans = [0] * len(nums)
        if len(zeros)>=2:
            return ans
        elif len(zeros) == 1:
            total = 1
            for n in nums:
                if n!=0:
                    total*=n
            ans[zeros[0]] = total
            return ans
        else:
            total = 1
            for n in nums:
                total *= n
            for i in range(len(nums)):
                nums[i] = total//nums[i]
            return nums