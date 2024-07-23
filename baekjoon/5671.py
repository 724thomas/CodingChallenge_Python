# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()


def solution(n, m):
    def check(n):
        visited = set()
        s = str(n)
        for c in s:
            if c in visited:
                return False
            visited.add(c)
        return True

    count = 0
    for i in range(n, m + 1):
        if check(i):
            count += 1

    return count


if __name__ == '__main__':
    while True:
        a = list(map(int, input().strip().split()))
        if not a:
            exit()
        n, m = a
        print(solution(n, m))
