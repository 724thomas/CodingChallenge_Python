# https://www.acmicpc.net/problem/5107

'''
1. 아이디어 :
    방문을 체크하면서 방문하지 않았으면, 방문체크후, 연결된 사람들을 방문 체크한다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
 해시셋, 해시맵
'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict, deque


def solution(frm_to):
    # print(*arr, sep="\n")
    visited = set()
    ans = []

    def check(person):
        nxt = frm_to[person]
        visited.add(nxt)
        while nxt != person:
            nxt = frm_to[nxt]
            visited.add(nxt)

    count = 0
    for frm, to in frm_to.items():
        if frm in visited:
            continue
        count += 1
        check(frm)

    return count


if __name__ == '__main__':
    count = 0
    while True:
        count += 1
        n = int(input())
        if n == 0:
            exit()
        frm_to = defaultdict(str)
        for _ in range(n):
            frm, to = list(input().strip().split())
            frm_to[frm] = to
        print(count, solution(frm_to))
