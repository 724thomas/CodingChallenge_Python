#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


# -------------------------------------------------------UserCode-------------------------------------------------------#
class Solution:
    def solution(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        n = []

        def dfs(node):
            if not node:
                return

            n.append(node)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        curr = root
        for i in range(1, len(n)):
            curr.left = None
            curr.right = n[i]
            curr = curr.right


# -------------------------------------------------------Converter Code-------------------------------------------------------#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def array_to_skip_null_parent_levelorder_tree(arr):
    if not arr:
        return None

    # Create a list of nodes, where each node corresponds to an element in the array
    nodes = [None if val is None else TreeNode(val) for val in arr]

    # Queue to keep track of parents
    parents = []

    # Variable to keep track of the current parent index
    next_parent_index = -1

    # Variable to keep track of the next child index
    next_child_index = 1

    # Start with the root node
    root = nodes[0]
    parents.append(root)

    # Iterate over the array and assign children to their parents
    for i in range(len(arr)):
        if nodes[i] is not None:
            # Find the next parent if needed
            while next_parent_index < len(parents) - 1 and next_child_index < len(arr):
                next_parent_index += 1
                parent = parents[next_parent_index]

                # Assign the left child
                if parent.left is None and next_child_index < len(arr):
                    parent.left = nodes[next_child_index]
                    if nodes[next_child_index] is not None:
                        parents.append(nodes[next_child_index])
                    next_child_index += 1

                # Assign the right child
                if parent.right is None and next_child_index < len(arr):
                    parent.right = nodes[next_child_index]
                    if nodes[next_child_index] is not None:
                        parents.append(nodes[next_child_index])
                    next_child_index += 1

    return root


# -------------------------------------------------------Key, Val-------------------------------------------------------#
root = [1, 2, 5, 3, 4, None, 6]
root = array_to_skip_null_parent_levelorder_tree(root)

answer = [1, None, 2, None, 3, None, 4, None, 5, None, 6]
answer = array_to_skip_null_parent_levelorder_tree(answer)


# -------------------------------------------------------answerCheckContent-------------------------------------------------------#
def are_trees_equal(root1, root2):
    # If both trees are empty, they are equal
    if root1 is None and root2 is None:
        return True

    # If one of the trees is empty, or the values of the current nodes are different
    if root1 is None or root2 is None or root1.val != root2.val:
        return False

    # Recursively check the left and right subtrees
    return are_trees_equal(root1.left, root2.left) and are_trees_equal(root1.right, root2.right)



Solution().solution(root)
user_answer = root
print(are_trees_equal(answer, user_answer))







class Solution:
    def solution(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        n=[]

        def dfs(node):
            if not node:
                return

            n.append(node)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        curr=root
        for i in range(1,len(n)):
            curr.left=None
            curr.right=n[i]
            curr=curr.right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def array_to_skipnull_levelorder_tree(arr):
    if not arr:
        return None

    # Create a list of nodes, where each node corresponds to an element in the array
    nodes = [None if val is None else TreeNode(val) for val in arr]

    # Queue to keep track of parents
    parents = []

    # Variable to keep track of the current parent index
    next_parent_index = -1

    # Variable to keep track of the next child index
    next_child_index = 1

    # Start with the root node
    root = nodes[0]
    parents.append(root)

    # Iterate over the array and assign children to their parents
    for i in range(len(arr)):
        if nodes[i] is not None:
            # Find the next parent if needed
            while next_parent_index < len(parents) - 1 and next_child_index < len(arr):
                next_parent_index += 1
                parent = parents[next_parent_index]

                # Assign the left child
                if parent.left is None and next_child_index < len(arr):
                    parent.left = nodes[next_child_index]
                    if nodes[next_child_index] is not None:
                        parents.append(nodes[next_child_index])
                    next_child_index += 1

                # Assign the right child
                if parent.right is None and next_child_index < len(arr):
                    parent.right = nodes[next_child_index]
                    if nodes[next_child_index] is not None:
                        parents.append(nodes[next_child_index])
                    next_child_index += 1

    return root
root = [0]
root = array_to_skip_null_parent_levelorder_tree(root)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def array_to_skipnull_levelorder_tree(arr):
    if not arr:
        return None

    # Create a list of nodes, where each node corresponds to an element in the array
    nodes = [None if val is None else TreeNode(val) for val in arr]

    # Queue to keep track of parents
    parents = []

    # Variable to keep track of the current parent index
    next_parent_index = -1

    # Variable to keep track of the next child index
    next_child_index = 1

    # Start with the root node
    root = nodes[0]
    parents.append(root)

    # Iterate over the array and assign children to their parents
    for i in range(len(arr)):
        if nodes[i] is not None:
            # Find the next parent if needed
            while next_parent_index < len(parents) - 1 and next_child_index < len(arr):
                next_parent_index += 1
                parent = parents[next_parent_index]

                # Assign the left child
                if parent.left is None and next_child_index < len(arr):
                    parent.left = nodes[next_child_index]
                    if nodes[next_child_index] is not None:
                        parents.append(nodes[next_child_index])
                    next_child_index += 1

                # Assign the right child
                if parent.right is None and next_child_index < len(arr):
                    parent.right = nodes[next_child_index]
                    if nodes[next_child_index] is not None:
                        parents.append(nodes[next_child_index])
                    next_child_index += 1

    return root
answer = [0]
answer = array_to_skip_null_parent_levelorder_tree(answer)
def are_trees_equal(root1, root2):
    # If both trees are empty, they are equal
    if root1 is None and root2 is None:
        return True

    # If one of the trees is empty, or the values of the current nodes are different
    if root1 is None or root2 is None or root1.val != root2.val:
        return False

    # Recursively check the left and right subtrees
    return are_trees_equal(root1.left, root2.left) and are_trees_equal(root1.right, root2.right)


Solution().solution(root)
user_answer = root
print(are_trees_equal(answer, user_answer))




outputString:
errorString:   File "<string>", line 3

^
SyntaxError: unexpected EOF while parsing
    bash: line 3: Do: command not found
bash: line 141: $'\n        n=[]\n        \n        def dfs(node):\n            if not node:\n                return\n            \n            n.append(node)\n            dfs(node.left)\n            dfs(node.right)\n        \n        dfs(root)\n        \n        curr=root\n        for i in range(1,len(n)):\n            curr.left=None\n            curr.right=n[i]\n            curr=curr.right\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\n\ndef array_to_skipnull_levelorder_tree(arr):\n    if not arr:\n        return None\n\n    # Create a list of nodes, where each node corresponds to an element in the array\n    nodes = [None if val is None else TreeNode(val) for val in arr]\n\n    # Queue to keep track of parents\n    parents = []\n\n    # Variable to keep track of the current parent index\n    next_parent_index = -1\n\n    # Variable to keep track of the next child index\n    next_child_index = 1\n\n    # Start with the root node\n    root = nodes[0]\n    parents.append(root)\n\n    # Iterate over the array and assign children to their parents\n    for i in range(len(arr)):\n        if nodes[i] is not None:\n            # Find the next parent if needed\n            while next_parent_index < len(parents) - 1 and next_child_index < len(arr):\n                next_parent_index += 1\n                parent = parents[next_parent_index]\n\n                # Assign the left child\n                if parent.left is None and next_child_index < len(arr):\n                    parent.left = nodes[next_child_index]\n                    if nodes[next_child_index] is not None:\n                        parents.append(nodes[next_child_index])\n                    next_child_index += 1\n\n                # Assign the right child\n                if parent.right is None and next_child_index < len(arr):\n                    parent.right = nodes[next_child_index]\n                    if nodes[next_child_index] is not None:\n                        parents.append(nodes[next_child_index])\n                    next_child_index += 1\n\n    return root\nroot = [0]\nroot = array_to_skip_null_parent_levelorder_tree(root)\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\n\ndef array_to_skipnull_levelorder_tree(arr):\n    if not arr:\n        return None\n\n    # Create a list of nodes, where each node corresponds to an element in the array\n    nodes = [None if val is None else TreeNode(val) for val in arr]\n\n    # Queue to keep track of parents\n    parents = []\n\n    # Variable to keep track of the current parent index\n    next_parent_index = -1\n\n    # Variable to keep track of the next child index\n    next_child_index = 1\n\n    # Start with the root node\n    root = nodes[0]\n    parents.append(root)\n\n    # Iterate over the array and assign children to their parents\n    for i in range(len(arr)):\n        if nodes[i] is not None:\n            # Find the next parent if needed\n            while next_parent_index < len(parents) - 1 and next_child_index < len(arr):\n                next_parent_index += 1\n                parent = parents[next_parent_index]\n\n                # Assign the left child\n                if parent.left is None and next_child_index < len(arr):\n                    parent.left = nodes[next_child_index]\n                    if nodes[next_child_index] is not None:\n                        parents.append(nodes[next_child_index])\n                    next_child_index += 1\n\n                # Assign the right child\n                if parent.right is None and next_child_index < len(arr):\n                    parent.right = nodes[next_child_index]\n                    if nodes[next_child_index] is not None:\n                        parents.append(nodes[next_child_index])\n                    next_child_index += 1\n\n    return root\nanswer = [0]\nanswer = array_to_skip_null_parent_levelorder_tree(answer)\ndef are_trees_equal(root1, root2):\n    # If both trees are empty, they are equal\n    if root1 is None and root2 is None:\n        return True\n\n    # If one of the trees is empty, or the values of the current nodes are different\n    if root1 is None or root2 is None or root1.val != root2.val:\n        return False\n\n    # Recursively check the left and right subtrees\n    return are_trees_equal(root1.left, root2.left) and are_trees_equal(root1.right, root2.right)\n\n\nSolution().solution(root)\nuser_answer = root\nprint(are_trees_equal(answer, user_answer))': command not found

