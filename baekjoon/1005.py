# https://www.acmicpc.net/problem/1005 ACM Craft

'''
1. 아이디어 :
    dp를 사용하지 않으면 시간초과
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    큐, 해시맵, 배열
'''
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


for _ in range(int(input())):
    structures, rules = list(map(int, input().split()))
    times = [0] + [int(num) for num in input().split()]
    seq = defaultdict(list)
    pre_req = [0 for _ in range(structures+1)]
    dp = defaultdict(int)

    for _ in range(rules):
        s, e = list(map(int, input().split()))
        seq[s].append(e)
        pre_req[e] += 1

    q = deque()
    for i in range(1, structures + 1):
        if pre_req[i] == 0:
            q.append(i)
            dp[i] = times[i]

    while q:
        structure = q.popleft()
        for i in seq[structure]:
            pre_req[i] -= 1
            dp[i] = max(dp[i], dp[structure] + times[i])
            if pre_req[i] == 0:
                q.append(i)

    print(dp[int(input())])
