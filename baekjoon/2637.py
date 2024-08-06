# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    2차원 배열과 degrees(필요 부품수)을 둔다.
    목표부품, 필수부품, 갯수를 순회하면서
    목표 부품을 만들기 위해 필요한 필수 부품들을 모두 배열에 저장한다.
2. 시간복잡도 :
    O( n ** 2 )
3. 자료구조 :
    해시셋, 해시맵, 2차원 배열
'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict, deque


def solution(n, m, arr):
    parts = defaultdict(list)
    degrees = [0] * (n+1)
    needs = [[0 for _ in range(n+1)]for _ in range(n+1)]
    fundamentals = set(range(1, n+1))
    for part, prev, amount in arr:
        parts[prev].append((part, amount))
        degrees[part] += 1
        fundamentals.discard(part)

    queue = deque()
    for part in fundamentals:
        queue.append(part)
        needs[part][part] = 1

    while queue:
        curr = queue.popleft()

        for nxt, amount in parts[curr]:
            for i in range(1, n+1):
                needs[nxt][i] += needs[curr][i] * amount
            degrees[nxt] -= 1
            if degrees[nxt] == 0:
                queue.append(nxt)

    print(needs[n])
    for i in range(1, n+1):
        if needs[n][i] != 0:
            print(i, needs[n][i])

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    arr = [list(map(int, input().strip().split())) for _ in range(m)]
    solution(n, m, arr)
