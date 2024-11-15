# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
from collections import defaultdict
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(n, arr):

    def preorder(node):
        if node == ".": return

        ans[0]+=node
        preorder(graph[node][0])
        preorder(graph[node][1])

    def inorder(node):
        if node == ".": return

        inorder(graph[node][0])
        ans[0]+=node
        inorder(graph[node][1])

    def postorder(node):
        if node ==".": return

        postorder(graph[node][0])
        postorder(graph[node][1])
        ans[0]+=node

    graph = defaultdict(list)

    for a, b, c in arr:
        graph[a] = [b,c]
    ans = [""]
    preorder("A")
    print(ans[0])
    ans = [""]
    inorder("A")
    print(ans[0])
    ans = [""]
    postorder("A")
    print(ans[0])



if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input().split())
    solution(n, arr)

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