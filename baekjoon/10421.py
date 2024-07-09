# https://www.acmicpc.net/problem/10421

'''
1. 아이디어 :
    시간 초과
2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

import sys
from itertools import product

def input():
    return sys.stdin.readline().rstrip()

# DFS를 이용하여 가능한 곱셈 결과를 찾는 함수
def dfs(a1, idx, total):
    global result
    if idx == stars[1]:
        str_total = str(total)
        str_set = set(str_total)
        if len(str_total) == stars[idx + 2] and not (str_set - total_num):
            result += 1
    else:
        for num in set_nums:
            partial_num = num * a1
            str_partial_num = str(partial_num)
            str_set = set(str_partial_num)
            print(str_partial_num, str_set)
            if len(str_partial_num) == stars[idx + 2] and not (str_set - total_num):
                number_of_digit = 10 ** idx
                temp_num = partial_num * number_of_digit
                dfs(a1, idx + 1, total + temp_num)

# 입력 처리
N = int(input())
list_ = input().split()
K = input()
list__ = input().split()
K = int(K)

# 라인 별 자리수 정보
stars = list(map(int, list_))
# 가능한 숫자 목록
nums = list__[:]
total_num = set(nums)
set_nums = set(map(int, nums))

result = 0

# 첫 번째 숫자 조합을 생성하고 DFS 호출
for num_line1 in product(nums, repeat=stars[0]):
    first_line_num = int(''.join(num_line1))
    dfs(first_line_num, 0, 0)

print(result)



'''
6
5 3 5 5 5 7
9
1 2 3 4 5 6 7 8 9
'''

#
# import sys
# #sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
#
#
# from itertools import product
# from collections import defaultdict
# def solution(N, stars, nums):
#     nums = set(nums)
#     combs = defaultdict(set)
#
#     def backtrack(s):
#         if len(s) > 5:
#             return
#         if len(s) != 0:
#             combs[len(s)].add(int(s))
#         for n in nums:
#             backtrack(s + str(n))
#
#     def check_num_included(n):
#         for c in str(n):
#             if int(c) not in nums:
#                 return False
#         return True
#
#     def check_valid_comb(a1, a2, sizes):
#         if len(str(a1*a2)) != sizes[-1]:
#             return False
#         if not check_num_included(a1*a2):
#             return False
#
#         a2_str = str(a2)
#         for i in range(len(a2_str)):
#             target = a1 * int(a2_str[len(a2_str)-1-i])
#             if len(str(target)) != sizes[i]:
#                 return False
#             if not check_num_included(target):
#                 return False
#         return True
#
#     backtrack("")
#     print(combs)
#     ans = 0
#     for a1 in combs[stars[0]]:
#         for a2 in combs[stars[1]]:
#             if check_valid_comb(a1, a2, stars[2:]):
#                 ans += 1
#     return ans
#
# N = int(input())
# stars = list(map(int, input().strip().split()))
# int(input())
# nums = list(map(int, input().strip().split()))
# print(solution(N, stars, nums))

