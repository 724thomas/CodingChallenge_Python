# https://www.acmicpc.net/problem/2747

'''
1. 아이디어 :
    1) 배열을 선언하여 memoization으로 연산한다.
    2) n<=45 이므로, 미리 정의를 하고 해당 인덱스 값을 반환해도 될것 같다.
2. 시간복잡도 :
    1) O(n)
3. 자료구조 :
    1) 배열
'''

import sys

input = sys.stdin.readline
n = int(input())
nums = [0] * 46
nums[1] = 1
for i in range(2, n + 1):
    nums[i] = nums[i - 1] + nums[i - 2]
print(nums[n])
