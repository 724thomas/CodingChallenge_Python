# https://leetcode.com/problems/sliding-window-maximum/description/

'''
1. 아이디어 :
    deque를 사용해서 시간복잡돌르 더 줄인다.
    l, r 포인터를 만들고, r이 k가될때까지 제일 큰 값의 index만 저장해놓는다.
    l과 r을 하나씩 증가시키면서 l이 q[0]보다 작으면 q[0]을 pop한다.

2. 시간복잡도 :
    O(n)

3. 자료구조 :
    deque
'''

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = r = 0
        ans = []

        while r<len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if r+1 >= k:
                ans.append(nums[q[0]])
                l+=1
            r+=1

        return ans