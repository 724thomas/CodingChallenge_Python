# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

from collections import deque, defaultdict
import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(n, arr):
    xs = defaultdict(int)
    ys = defaultdict(int)
    for x, y in arr:
        xs[x] += 1
        ys[y] += 1

    def get_min(dict):
        curr = 0
        start = min(dict)
        for k, v in dict.items():
            curr += abs(start-k) * v

        left = 0
        right = len(arr)
        ans = float('inf')
        for i in range(min(dict), max(dict)+1):
            ans = min(ans, curr)
            left += dict[i]
            right -= dict[i]
            curr = curr - right + left
        return ans

    return get_min(xs) + get_min(ys)


if __name__ == '__main__':
    # n, m = map(int, input().split())
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(solution(n, arr))

