# https://www.acmicpc.net/problem/1806
'''
1. 아이디어 :
    1) lp=rp=0으로 설정 후, target보다 크거나 같으면 total-=alist[lp]을 하고
     lp+=1을 한 후 길이를 구하고(rp-lp+1) current min을 갱신한다.
    작으면 total+=alist[rp]로 갱신하고 rp+=1 한다.
2. 시간복잡도 :
    1) O(n)
    - while문
3. 자료구조 :
    1) 배열
'''
import sys
n, target = map(int, sys.stdin.readline().split())
alist = list(map(int, sys.stdin.readline().split()))
lp = 0
rp = 0
total = alist[0]
min_length = float('inf')

while True:
    if total >= target:
        total -= alist[lp]
        min_length = min(min_length, rp - lp + 1)
        lp+=1
    elif total < target:
        rp += 1
        if rp == n:
            break
        total += alist[rp]
print(min_length if min_length != float('inf') else 0)
