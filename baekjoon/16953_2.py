# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(n, m):
    # print(*arr, sep="\n")
    # queue
    queue = [(n, 1)]
    visited = set()

    while queue:
        num, count = queue.pop(0)
        if num == m:
            return count

        if num in visited: continue
        visited.add(num)

        if num * 2 <= m:
            queue.append((num * 2, count + 1))
        if num * 10 + 1 <= m:
            queue.append((num * 10 + 1, count + 1))
    return -1



if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solution(int(n), int(m)))

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