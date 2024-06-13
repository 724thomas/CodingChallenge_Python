# https://www.acmicpc.net/problem/15659

'''
1. 아이디어 :
    백트래킹으로 조합구하고, deque로 연산자 순서에 따른 연산
2. 시간복잡도 :
    O( 2**n )
3. 자료구조 :
    deque
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import deque
def solution(n, nums, c):
    combinations = set()
    coms = {"+": c[0], "-": c[1], "*": c[2], "/": c[3]}

    def backtrack(s):
        if len(s) >= len(nums) - 1:
            combinations.add(s)
            return

        for k, v in coms.items():
            if v != 0:
                coms[k] -= 1
                backtrack(s + k)
                coms[k] += 1

    def calc(nums, combination):
        queue = deque()
        queue.append(nums[0])
        for i in range(len(combination)):
            if combination[i] == "+":
                queue.append("+")
                queue.append(nums[i+1])
            elif combination[i] == "-":
                queue.append("-")
                queue.append(nums[i+1])
            elif combination[i] == "*":
                queue[-1] *= nums[i+1]
            else:
                queue[-1] = queue[-1] // nums[i+1]

        while len(queue) != 1:
            left = queue.popleft()
            command = queue.popleft()
            right = queue.popleft()
            if command == "+":
                queue.appendleft(left+right)
            else:
                queue.appendleft(left-right)
        return queue[0]

    backtrack("")
    cmin = float('inf')
    cmax = -float('inf')
    for c in combinations:
        res = calc(nums, c)
        cmin = min(cmin, res)
        cmax = max(cmax, res)

    print(cmax)
    print(cmin)


n = int(input())
nums = list(map(int, input().strip().split()))
coms = list(map(int, input().strip().split()))
solution(n, nums, coms)


# http://colorscripter.com/s/VUktwnY