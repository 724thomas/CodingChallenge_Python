# https://www.acmicpc.net/problem/2805


'''
1. 아이디어 :
    1) 이분탐색 문제다. 최소1, 최대max(tree)로 해당 지점에서 잘랐을때의 합을 구하면서 탐색을 한다.
2. 시간복잡도 :
    1) Constructor: O(n), getRandom: O(1)
3. 자료구조 :
    1) 이분탐색a
'''
import sys

n, target = map(int, sys.stdin.readline().rstrip().split())
tree = list(map(int, sys.stdin.readline().split()))
lp, rp = 1, max(tree)

while lp <= rp:
    cmin = (lp + rp) // 2
    cut = sum([x - cmin for x in tree if x > cmin])
    if cut >= target:
        lp = cmin + 1
    else:
        rp = cmin - 1
print(rp)
