#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        cmax = max([interval[1] for interval in intervals])
        dp = [0] * (cmax+2)
        ans = 0
        curr = 0

        for start, end in intervals:
            dp[start] += 1
            dp[end] -= 1
        for i in range(1, len(dp)):
            dp[i] += dp[i-1]
        return max(dp)