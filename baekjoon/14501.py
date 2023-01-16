# https://www.acmicpc.net/problem/14501

'''
1. 아이디어 :
    1) dp문제이지만 다르게 풀어봤다. queue를 사용. t는 5까지 받으므로 n+6배열을 선언.
    들어오는 t, p입력마다, t인덱스에 현재 값과, 받은 p+current max 값중 큰 값을 넣고,
    왼쪽으로 한칸씩 이동시킨다. cmax를 0인덱스랑 비교하여 갱신한다.
2. 시간복잡도 :
    1) O(n) + O(n) = O(n)
    - N번만큼 배열에 0을 넣는다. + 입력N번만큼 반복문을 돈다.
3. 자료구조 :
    1) 큐
'''

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
nums, cmax = deque([0] * (n + 6)), 0
for i in range(n):
    t, p = map(int, input().split())
    nums[t] = max(nums[t], p + cmax)
    nums.popleft()
    nums.append(0)
    cmax = max(cmax, nums[0])
print(cmax)
