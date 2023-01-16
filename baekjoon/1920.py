# https://www.acmicpc.net/problem/1920

'''
1. 아이디어 :
    1) 이진탐색을 이용
    2) 중복을 제거해주는 set()을 이용
2. 시간복잡도 :
    1) 이진탐색 -  O(nlogn) + O(mlogn)= O(nlogn)
    - n : n개의 원소를 Sorting에 걸리는 시간 + m : m번 탐색에 걸리는시간
    2 ) set() - O(n) + O(m) = O(n)
    - n : n개에 원소를 set에 넣는데 걸리는 시간 (1) + m : m개의 원소를 set에서 찾는데 걸리는 시간 (1)
3. 자료구조 :
    1) 이진탐색
    2) set()
'''


import sys
import bisect
input()
nums = list(map(int, sys.stdin.readline().split()))
input()
check = list(map(int, sys.stdin.readline().split()))
print(nums)
print(check)
for i in check:
    print(bisect.insort_left(nums, i))


#
# #1)
# import sys
# numbers = set()
# noneed1, save_numbers, noneed2, check_numbers = input(), list(map(int, sys.stdin.readline().split())), input(), list(map(int, sys.stdin.readline().split()))
# for save_number in save_numbers:
#     numbers.add(save_number)
# for check_number in check_numbers:
#     print(1 if check_number in numbers else 0)
#
#
#
#
# #2)
# def binarySearch(alist, target):
#     start = 0
#     end = len(alist)-1
#     while start <= end:
#         mid = (start + end) // 2
#         if alist[mid] == target:
#             return 1
#         elif alist[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return 0
#
# n = int(sys.stdin.readline())
# alist = list(map(int, sys.stdin.readline().split()))
# alist.sort()
# m = int(sys.stdin.readline())
# blist = list(map(int, sys.stdin.readline().split()))
# for i in blist:
#     print(binarySearch(alist, i))
#
#
#


