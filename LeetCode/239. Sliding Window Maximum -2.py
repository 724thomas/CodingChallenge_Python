# https://leetcode.com/problems/sliding-window-maximum/description/

'''
1. 아이디어 :
    monotonic stack을 사용한다.
    stack에는 index를 저장하고, queue에 nums[i]를 저장한다.
    nums[i] > nums[stack[-1]]일때 계속해서 stack에서 pop한다.
    i-k+1이 stack[0](인덱스) 보다 커지면 범위를 벗어나므로 pop한다.
    ans에는 nums[stack[0]]을 append한다.
    ans[k-1:]을 리턴한다.
2. 시간복잡도 :
    O(N)
3. 자료구조 :
    큐
'''

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        ans = []

        for i in range(len(nums)):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            if queue[0] < i-k+1:
                queue.popleft()

            ans.append(nums[queue[0]])

        return ans[k-1:]
