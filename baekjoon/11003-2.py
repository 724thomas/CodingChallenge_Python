# https://www.acmicpc.net/problem/11003 최소값 찾기

'''
1. 아이디어 :
    투포인터와 힙을 쓰면 시간초과가 난다.
    monotonic stack 사용
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    스택
'''
from collections import deque
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, m, nums):
    queue = deque()
    ans = []
    for i in range(len(nums)):
        while queue and queue[-1][0] > nums[i]:
            queue.pop()
        queue.append((nums[i], i))
        if queue[0][1] < i-m+1:
            queue.popleft()
        ans.append(queue[0][0])
    return ans


n, m = list(map(int, input().split()))
integer_list = [int(num) for num in input().split()]
print(*solution(n, m, integer_list))
