# https://www.acmicpc.net/problem/9461

'''
1. 아이디어 :
    1) 배열을 선언하여 memoization으로 연산한다. 여러개의 케이스가 들어가므로, 연산한 값이 있다면 그 값을 사용하게 한다.
2. 시간복잡도 :
    1) O(n) * O(n) = O(n^2)
    - case 갯수 * memoization 연산 갯수
3. 자료구조 :
    1) 배열
'''

import sys

input = sys.stdin.readline
nums = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
nums = [-1] * 101
nums[0] = nums[1] = nums[2] = 1
for _ in range(int(input())):
    n = int(input())
    for i in range(3, n):
        if nums[i] == -1:
            nums[i] = nums[i - 2] + nums[i - 3]
    print(nums[n-1])
