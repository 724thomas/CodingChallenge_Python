# https://www.acmicpc.net/problem/3273

'''
1. 아이디어 :
    1) 입력된 수를 배열에 넣고 정렬한 후, lp=0, rp=n-1로 설정하고 
    [lp]+[rp]의 합이 target보다 크면 rp-=1, 작으면 lp+=1, 같으면 count+=1, 양쪽 포인터 모두 이동.
2. 시간복잡도 :
    1) O(nlogn) + O(n) = O(nlogn)
    - n개의 원소를 정렬 + while문
3. 자료구조 :
    1) 배열
'''# https://www.acmicpc.net/problem/3273

import sys
n = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))
count, lp, rp = 0, 0, n-1
target = int(sys.stdin.readline())
print(nums)
while lp <rp:
    temp = nums[lp] + nums[rp]
    if temp == target:
        count+=1
        lp+=1
        rp-=1
    elif temp > target:
        rp-=1
    elif temp < target:
        lp+=1
print(count)