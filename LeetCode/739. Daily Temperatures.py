#

'''
1. 아이디어 :
    스택을 사용한다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    스택
'''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                val = stack.pop()
                ans[val] = i - val
            stack.append(i)
        return ans





