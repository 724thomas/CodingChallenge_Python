# https://www.acmicpc.net/problem/2230
'''
1. 아이디어 :
    1) 입력값을 배열에 넣고 정렬. current min을 최대로 잡아 놓고,
    lp=0, rp=1로 설정 후, while lp,rp<m 조건으로 반복문을 돌린다. target보다 작으면 lp+=1, 크면 rp+=1 한 후 current min과 비교하여 갱신한다.
2. 시간복잡도 :
    1) O(nlogn) + O(n) = O(nlogn)
    - n개의 원소를 정렬 + while문
3. 자료구조 :
    1) 배열
'''
import sys
n, m = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.sort()
if n == 1:
    print(0)
    sys.exit()

cmin = float('inf')
lp = 0
rp = 1
while lp < n and rp < n:
    diff = nums[rp] - nums[lp]
    if diff < m:
        rp += 1
    else:
        lp += 1
        cmin = min(cmin, diff)
print(cmin)
