#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        nodes=deque()
        nodes.append([root,0])
        self.check=float('inf')
        while nodes:
            n=nodes.popleft()
            node=n[0]
            level=n[1]

            if node.val==u.val:
                self.check=level
                break
            if node.left:
                nodes.append([node.left,level+1])
            if node.right:
                nodes.append([node.right,level+1])

        if len(nodes)==0:
            return None
        if nodes[0][1]==self.check:
            return nodes[0][0]
        return None