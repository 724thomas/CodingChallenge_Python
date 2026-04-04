# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 / 알고리즘 :

'''


import sys
from collections import defaultdict
from queue import Queue

#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()
nodes = defaultdict(list)
n = 0
def solution():
    par_map = defaultdict(int)
    queue = Queue()
    queue.put(1)
    visited = set()
    visited.add(1)

    while not queue.empty():
        node = queue.get()
        for nextNode in nodes[node]:
            if nextNode in visited: continue
            visited.add(nextNode)
            par_map[nextNode] = node
            queue.put(nextNode)

    for i in range(2, n+1):
        print(par_map[i])
    return



if __name__ == '__main__':
    n = int(input().rstrip())
    for _ in range(n-1):
        a, b = map(int, input().split())
        nodes[a].append(b)
        nodes[b].append(a)
    solution()

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