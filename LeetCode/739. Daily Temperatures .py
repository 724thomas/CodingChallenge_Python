# https://leetcode.com/problems/daily-temperatures/description/

'''
1. 아이디어 :
    monotonic_stack을 사용한다.
    stack에는 [온도, 인덱스]를 저장한다.
    stack의 마지막 온도보다 낮으면 stack에 저장하고,
    마지막 온도보다 높으면 하나씩 꺼내면서 인덱스를 정답 배열에 저장한다.
2. 시간복잡도 :
    O(n) + O(n) = O(n)
3. 자료구조 :
    배열
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        monotonic_stack = []
        for i,t in enumerate(temperatures):
            while monotonic_stack and t > monotonic_stack[-1][0]:
                stackT, stackInd = monotonic_stack.pop()
                ans[stackInd] = (i-stackInd)
            monotonic_stack.append([t,i])
        return ans