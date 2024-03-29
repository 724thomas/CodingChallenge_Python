# https://www.acmicpc.net/problem/5639

'''
1. 아이디어 :
    1) (시간초과...왜???) 입력값들을 이진트리에 넣는다. 후위순회를 재귀를 이용하여 구현.
    2) 첫번쨰 입력값이 root니까, 재귀용법으로 root 기준으로 둘로 나눈다. root제외 다른 값이 없으면 출력.
2. 시간복잡도 :
    1) O(n) + O(n) + O(n) = O(n)
    - 입력 받아서 리스트에 넣는 시간복잡도 : O(n), 이진트리에 입력하는 시간복잡도 : O(n), 후위순회 : O(n)
    2) O(n) + O(n) = O(n)
    - 입력 받아서 리스트에 넣는 시간복잡도 : O(n), 재귀함수 안에 for문.
3. 자료구조 :
    1) 이진 검색 트리
'''

import sys
sys.setrecursionlimit(10**9)
nums = []
while True:
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break
def dfs(start, end):
    if start > end:
        return
    base = nums[start]
    mid = end+1
    for i in range(start+1, end+1):
        if base < nums[i]:
            mid = i
            break

    dfs(start+1, mid-1)
    dfs(mid, end)
    print(base)

dfs(0, len(nums)-1)

'''


2)
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = Node(val)
            return
        elif val > self.val:
            if self.right:
                self.right.insert(val)
                return
            self.right = Node(val)



def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node.val)

import sys
sys.setrecursionlimit(10**9)
nums = []
while True:
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break

root = Node(nums[0])
for i in range(1, len(nums)):
    root.insert(nums[i])

postorder(root)

len = 9
50, [30,24,5,28,45] [98,52,60]

30 [24,5,28] [45]    98 [52,60] []

24 [5] [28]    45 [] []     52  [60]

5 [] []     28 [] []     45 [] []     60 [] []
'''