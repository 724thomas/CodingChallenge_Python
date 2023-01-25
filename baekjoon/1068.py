# https://www.acmicpc.net/problem/1068

'''
1. 아이디어 :
    1) 트리를 먼저 만들고, 각 노드안에 자식노드들의 총 리프노드 값을 저장한다.
2. 시간복잡도 :

3. 자료구조 :

'''


import sys
input = sys.stdin.readline

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self. val = val
        self.left = left
        self.right = right

nodes = int(input())
nums = list(map(int, input().split(' ')))
k = int(input())
print(nums, k)
nodes_total = [1] * nodes

root = TreeNode()
for i in range(len(nums)):
    nodes_total[i] = nums.count(i)
total = nodes_total.count(0)
print(nodes_total)
print(total, nodes_total[k], total-nodes_total[k])

'''
9
-1 0 0 2 2 4 4 6 6
4
'''
