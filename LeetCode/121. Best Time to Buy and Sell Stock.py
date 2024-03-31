#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        ans = 0
        for p in prices:
            while stack and stack[-1] > p:
                stack.pop()
            stack.append(p)
            ans = max(ans, p-stack[0])
        return ans