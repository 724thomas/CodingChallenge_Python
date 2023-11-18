# https://www.acmicpc.net/problem/5639

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


nodes = []
while True:
    num = input()
    if num:
        nodes.append(int(num))
    else:
        break

print(nodes)
