# https://www.acmicpc.net/problem/11003

'''
1. 아이디어 :
    1) (시간초과) 슬라이딩 윈도우로 매번 min값을 구해주면 된다.
    2) (시간초과)최소값을 다른방법으로 구해야될 것 같다.
    슬라이딩 윈도우 대신, 인덱스와 값을 배열에 append하고,
    배열에 있는 값들이 다음 들어오는 값보다 작으면 모두 pop을 한다.
    그리고 제일 처음에 들어왔던 값이, l의 범위를 벗어나면 pop한다.
    3) 배열을 사용하지 않고, collections deque를 사용해서 풀어보자.
2. 시간복잡도 :
    1) O(n) * O(n) = O(n^2)
    - 슬라이딩 윈도우 반복문 * 최소값
    2) O(n)
    - 슬라이딩 윈도우 반복문
3. 자료구조 :
    1) 배열
    2) 배열
'''

import sys
from collections import deque
input = sys.stdin.readline
n, l = map(int, input().split())
nums = list(map(int, input().split()))
q = deque()
for i in range(n):
    while q and q[-1][1] > nums[i]:
        q.pop()
    q.append((i, nums[i]))
    if q[0][0] <= i - l:
        q.popleft()
    print(q[0][1], end=' ')


# 2)
# import sys
# input = sys.stdin.readline
# n, l = map(int, input().split())
# nums = list(map(int, input().split()))
# q = []]
# for i in range(n):
#     while q and q[-1][1] > nums[i]:
#         q.pop()
#     q.append((i, nums[i]))
#     if q[0][0] <= i - l:
#         q.popleft()
#     print(q[0][1], end=' ')

# import sys
# from collections import deque
# input = sys.stdin.readline
# n, l = map(int, input().split())
# nums = list(map(int, input().split()))
# q = deque(nums[:l])
# print(q)
# for _ in range(n):
#     q.popleft()
#     q.append(nums[_])
#     print(min(q), end=' ')