# https://www.acmicpc.net/problem/6159

'''
1. 아이디어 :
    1) 이중 포문을 돌면서 모든 경우의 수를 구한다
    2) 두 포인터로 lp=0, rp=n-1로 지정하고, while문안에 lp와 rp가 같아질때까지, [lp]+[rp]가 target보다 작거나 같아질때까지 반복한 후, lp와 rp 사이의 숫자들 +1을 ans에 더해준다.
2. 시간복잡도 :
    1) O(n^2)
    - 이중 포문
    2) O(logn) * O(n) = O(nlogn)
    - 정렬 + while문
3. 자료구조 :
    1) 배열
    2) 배열
'''

import sys

input = sys.stdin.readline
n, target = map(int, input().split())
cows = sorted([int(input()) for _ in range(n)])
ans = 0
lp = 0
rp = n - 1
while 1:
    if lp==rp:
        break
    if cows[lp] + cows[rp] > target:
        rp -= 1
    elif cows[lp] + cows[rp] <= target:
        ans += rp - lp
        lp += 1
print(ans)
#===============================================================================
input = sys.stdin.readline
n, target = map(int, input().split())
cows = [int(input()) for _ in range(n)]
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        if cows[i]+cows[j] <= target:
            ans+=1
        else:
            break
print(ans)
