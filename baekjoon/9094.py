# https://www.acmicpc.net/problem/9094

'''
1. 아이디어 :
    1) 100보다 작으므로 브루트포스로 풀면된다.
2. 시간복잡도 :
    1) O(n) * O(n) = O(n^2)
3. 자료구조 :
    1) -
'''

import sys
input = sys.stdin.readline
memoization = [[-1] * 101 for _ in range(101)]
for _ in range(int(input())):
    n, m = map(int, input().split())
    cnt = 0
    for a in range(1, n):
        for b in range(a + 1, n):
            if memoization[a][b]:
                cnt +=1
            else:
                if (a * a + b * b + m) % (a * b) == 0:
                    memoization[a][b] = 1
                    cnt += 1
                else:
                    memoization[a][b] = 0
    print(cnt)