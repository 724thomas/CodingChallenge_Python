# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    백트래킹을 이용해서 각 자리수마다 반전 가능한 수가 P보다 작은 경우를 찾는다.
2. 시간복잡도 :
    O( N ** K )
3. 자료구조 / 알고리즘:
맵, 리스트, 백트래킹
'''


import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()
ans = 0
n = k = p = x = 0
x_str = ""

def solution(): # N층(1<=N<=10**6), K자리(1<=K<=6), P반전 가능(1<=P<=42), X현재 층(1<=X<=10**6)
    global ans, n, k, p, x, x_str
    ans = 0

    map = defaultdict(list)
    map[0] = [0, 4, 3, 3, 4, 3, 2, 3, 1, 2]
    map[1] = [-1, 0, 5, 3, 2, 5, 6, 1, 5, 4]
    map[2] = [-1, -1, 0, 2, 5, 4, 3, 4, 2, 3]
    map[3] = [-1, -1, -1, 0, 3, 2, 3, 2, 2, 1]
    map[4] = [-1, -1, -1, -1, 0, 3, 4, 3, 3, 2]
    map[5] = [-1, -1, -1, -1, -1, 0, 1, 4, 2, 1]
    map[6] = [-1, -1, -1, -1, -1, -1, 0, 5, 1, 2]
    map[7] = [-1, -1, -1, -1, -1, -1, -1, 0, 4, 3]
    map[8] = [-1, -1, -1, -1, -1, -1, -1, -1, 0, 1]
    map[9] = [-1, -1, -1, -1, -1, -1, -1, -1, -1, 0]

    for row in range(10):
        for col in range(row, 10):
            if map[col][row] == -1:
                map[col][row] = map[row][col]

    x_str = str(x).zfill(k)
    backtrack(p, 0, 0, map)
    return ans

def backtrack(remain_p, index, curr, map):
    global ans, n, k, p, x, x_str

    if curr > n: return # 층 초과

    if index == k: # 자리수 초과
        if 1<=curr<=n and curr != x:
            ans+=1
        return

    index_num = int(x_str[index])

    for digit in range(10):
        digit_diff = map[index_num][digit]
        if digit_diff > remain_p: continue

        curr += digit * (10 ** (k-1-index))

        backtrack(remain_p - digit_diff, index+1, curr, map)

        curr -= digit * (10 ** (k-1-index))


if __name__ == '__main__':
    n, k, p, x = map(int, input().split())
    print(solution())

# n = int(input().rstrip())
#
# n, m = map(int, input().split())
# n, m = list(map(int, input().split()))
# a = [c for c in input().strip()]
#
# s = input().rstrip()

# arr = list(map(int, input().strip().split()))
# arr = tuple(map(int, input().split()))
# integer_list = [int(num) for num in input().split()]
# dp = [[0 for _ in range(n)] for _ in range(n)]
# dp = [[0 for j in range(n)] for i in range(n)]
# grid = [list(input().rstrip()) for _ in range(n)] # "aaa" "bbb"
# grid = list(list(map(int, input().split())) for _ in range(n)) # "0 0 0 0", "0 0 0 0"