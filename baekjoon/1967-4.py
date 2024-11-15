# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
from collections import defaultdict, deque
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(n, arr):

    def bfs(start_node):
        visited = set()
        visited.add(start_node)
        queue = deque()
        queue.append([start_node, 0])

        ans = [-1, -1]
        while queue:
            currNode, totalDistance = queue.popleft()
            if totalDistance > ans[1]:
                ans = [currNode, totalDistance]

            for next_node, distance in distances[currNode]:
                if next_node in visited: continue
                visited.add(next_node)
                queue.append([next_node, totalDistance + distance])
        return ans

    distances = defaultdict(set)

    for a, b, d in arr:
        distances[a].add((b,d))
        distances[b].add((a,d))

    farthest_node, _ = bfs(1)
    _, farthest_distance = bfs(farthest_node)

    return farthest_distance



if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n-1):
        arr.append(list(map(int, input().split())))
    print(solution(n, arr))

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