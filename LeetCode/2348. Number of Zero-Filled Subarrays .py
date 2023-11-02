# https://leetcode.com/problems/number-of-zero-filled-subarrays/description/

'''
1. 아이디어 :
    dp[i] = i개의 0으로 이루어진 subarray의 개수
    0을 만나면 count를 증가시키고, 0이 아닌 수를 만나면
    dp[count]를 정답에 더해주고 count를 0으로 초기화한다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    배열
'''

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [0] * (len(nums)+1)
        dp[1] = 1
        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + i

        count = 0
        ans = 0
        for n in nums:
            if n == 0:
                count+=1
            else:
                ans += dp[count]
                count=0
        ans += dp[count]
        return ans