# https://www.acmicpc.net/problem/18511

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

def solution(n, m, nums):

    candid = set()

    def backtrack(s):
        if int(s) > n:
            return

        candid.add(int(s))
        for num in nums:
            backtrack(s+str(num))

    backtrack("0")
    return max(candid)

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    print(solution(n, m, nums))


