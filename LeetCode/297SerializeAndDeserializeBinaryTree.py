#https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

'''
1. 아이디어 :
    1) dfs로 풀 수 있다. preOrder로 serialize를 정의하고, 마지막 string으로 만들어준 값을 return한다.
    deserialize에서는 string을 배열로 바꾼다음, index를 지정하여, 하나씩 증가하면서 left, right를 재귀용법으로 한다.
2. 시간복잡도 :
    1) O(n), O(n)
3. 자료구조 :
    1) 이진트리
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        nums = data.split(",")
        self.i = 0
        print(nums)
        def dfs():
            if nums[self.i]=="N":
                self.i +=1
                return None
            node = TreeNode(int(nums[self.i]))
            self.i +=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))