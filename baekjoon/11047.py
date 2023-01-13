# https://www.acmicpc.net/problem/11047

'''
1. 아이디어 :
    1) Greedy 알고리즘을 사용한다. 들어오는 값들을 내림차순 정렬 후, count+=price//가장큰값을 하고
    price를 갱신한다.
2. 시간복잡도 :
    1) O(n) + O(n) = O(n)
    - 정렬 + 반복문
3. 자료구조 :
    1) 배열
'''

import sys
n, price = map(int, sys.stdin.readline().split())
nums, count = list(int(sys.stdin.readline()) for _ in range(n)), 0
for i in range(len(nums)-1, -1, -1):
    if price >= nums[i]:
        count += price // nums[i]
        price %= nums[i]
print(count)