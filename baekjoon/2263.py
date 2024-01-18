# https://www.acmicpc.net/problem/2263 트리의 순회

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input().rstrip())
inorder = [int(num) for num in input().split()]
postorder = [int(num) for num in input().split()]





def solution(inorder, postorder):
    inorder_index = {num: idx for idx, num in enumerate(inorder)}
    preorder_list = []

    def dfs(inorder_start, inorder_end, postorder_start, postorder_end):
        if inorder_start > inorder_end or postorder_start > postorder_end:
            return

        root_val = postorder[postorder_end]
        preorder_list.append(root_val)  # Add root to preorder list
        root_index = inorder_index[root_val]

        left_tree_size = root_index - inorder_start
        right_tree_size = inorder_end - root_index

        # Recurse for left subtree
        dfs(inorder_start, root_index - 1, postorder_start, postorder_start + left_tree_size - 1)
        # Recurse for right subtree
        dfs(root_index + 1, inorder_end, postorder_end - right_tree_size, postorder_end - 1)

    dfs(0, len(inorder) - 1, 0, len(postorder) - 1)
    return preorder_list

print(*solution(inorder, postorder))


