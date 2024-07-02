# https://www.acmicpc.net/problem/6209

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(stones, n, m):
    def check(target):
        counts = 0
        curr_distance = 0
        for i in range(1, len(stones)):
            curr_distance += stones[i] - stones[i-1]
            if curr_distance < target:
                counts += 1
                if counts > m:
                    return False
            else:
                curr_distance = 0
        return True


    stones.sort()
    left = 0
    right = stones[-1]
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans


s, n, m = list(map(int, input().split()))
stones = [0]
for _ in range(n):
    stones.append(int(input()))
stones.append(s)
print(solution(stones, n, m))
