# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(heights):
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

heights = []
for _ in range(int(input())):
    heights.append(int(input()))
print(solution(heights))


