#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        s = startValue
        t = destValue
        def dfs(node, path, target):
            if not node:
                return ""
            if node.val == target:
                return path

            path.append("L")
            ans = dfs(node.left, path, target)
            if ans:
                return ans

            path.pop()
            path.append("R")
            ans = dfs(node.right, path, target)
            if ans:
                return ans
            path.pop()
            return ""

        start_path =  dfs(root, [], startValue)
        dest_path = dfs(root, [], destValue)
        i = 0
        while i < min(len(start_path), len(dest_path)):
            if start_path[i] != dest_path[i]:
                break
            i += 1

        ans = ["U"] * len(start_path[i:]) + dest_path[i:]
        return "".join(ans)



