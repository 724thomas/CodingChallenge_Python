#

'''
1. 아이디어 :
    1. 스택을 사용한다.
    2. 증가하는 순서이므로, while문에서 현재 높이보다 큰 높이를 가진 애들을 뽑는다.
    3. while문에서 start를 갱신해서 스택에 저장하는 이유는 나중에 뽑게되면 해당 idx 왼쪽에 있는 애들까지 모두 계산해야하므로.
    4. 마지막 loop에서 스택에 저장되어있는 애들을 모두 계산. for i, h in enumerate(stack)는 i가 아닌 저장된 start를 기준.
2. 시간복잡도 :
    O(  n )
3. 자료구조 :
    스택
'''



class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []

        for curr_idx, curr_height in enumerate(heights):
            start = curr_idx

            while stack and stack[-1][1] > curr_height:
                prev_idx, prev_height = stack.pop()
                ans = max(ans, prev_height * (curr_idx - prev_idx))
                start = prev_idx

            stack.append((start, curr_height))

        for curr_idx, curr_height in stack:
            ans = max(ans, (len(heights) - curr_idx) * curr_height )


        return ans