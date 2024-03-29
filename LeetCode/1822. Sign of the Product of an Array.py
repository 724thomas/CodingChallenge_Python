# https://leetcode.com/problems/sign-of-the-product-of-an-array/description/

'''
1. 아이디어 :
    nums를 순회하면서 음수이면 count를 증가시키고, 0이면 0을 반환한다.
    count가 짝수이면 1을 반환하고, 홀수이면 -1을 반환한다.
2. 시간복잡도 :
    O(N)
3. 자료구조 :
    배열
'''


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if num == 0:
                return 0
            elif num < 0 :
                count += 1
        return 1 if count%2==0 else -1