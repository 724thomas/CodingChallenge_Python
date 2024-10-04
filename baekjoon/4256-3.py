# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(n, preorder, inorder):
    in_map = {}
    for i, num in enumerate(inorder):
        in_map[num] = i

    def postorder(pre_left, pre_right, in_left, in_right):

        if pre_left > pre_right or in_left > in_right: return []

        root = preorder[pre_left]
        mid_idx = in_map[root]

        left_size = mid_idx - in_left

        left_arr = postorder(pre_left+1, pre_left + left_size, in_left, mid_idx-1)
        right_arr = postorder(pre_left+left_size+1, pre_right, mid_idx+1, in_right)
        return left_arr + right_arr + [root]

    return postorder(0, n-1, 0, n-1)

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        pre = list(map(int, input().split()))
        post = list(map(int, input().split()))
        print(*solution(n, pre, post))