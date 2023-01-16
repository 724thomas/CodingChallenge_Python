# https://www.acmicpc.net/problem/10942

'''
1. 아이디어 :
    1) (시간초과) 들어오는 숫자를 chr로 바꾼 후 하나의 String을 만들어준다. [s-1:e]와 [s-1:e][::-1]을 비교한다.
    2) (시간초과) 문자열 슬라이싱에서 시간초과가 나는것 같다. 명령을 입력받기전에 미리 처리해놔야할것 같아서, 2차원 배열을 만들어서
    해당 인덱스의 숫자가 팰린드롬인지 아닌지를 저장한다.
    3)  저장하는 방식에서 시간초과가 나는 것 같다. 0~5까지의 문자열이 팔린드롬이면, 1~4, 2~3도 팔린들롬인걸 알 수 있다.
    2차원 배열을 Memoization 방식으로 채워야할것 같다.
2. 시간복잡도 :
    1) O(n) + O(m) * O(e-s) = O(max(n,m*(e-s)))
    - chr로 바꾼다 + 비교하는 입력 * 문자열 슬라이싱
    2) O(n) + O(m) * O(m-1) * O(e-s) = O(max(n,n^2*(e-s)))
    - chr로 바꾼다 + 인덱스마다 슬라이싱 한다
    3) O(n) + O(n) + O(n) * O(n) + O(m)= O(n^2)
    - 길이1 슬라이스 1로 만든다 + 길이2 팔렌드롬 체크 + 2차 배열을 채운다.*O(n^2) + 명령수
3. 자료구조 :
    1) 문자열
    2) 2차원 배열
    3) 2차월 배열
'''

import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
pal_list = [[0] * n for _ in range(n)]
for i in range(n):
    pal_list[i][i] = 1
for i in range(n-1):
    if nums[i] == nums[i+1]:
        pal_list[i][i+1] = 1
for i in range(2, n):
    for j in range(n-i):
        if nums[j] == nums[i+j] and pal_list[j+1][i+j-1]:
            pal_list[j][j+i] = 1
for _ in range(int(input())):
    s, e = map(int, input().split())
    print(pal_list[s-1][e-1])

# 2)
# n = int(input())
# nums = list(map(int, input().split()))
# chars = "".join([chr(num) for num in nums])
# pal_list = [[0] * n for _ in range(n)]
# for i in range(len(nums)):
#     for j in range(i, len(nums)):
#         if chars[i:j+1] == chars[i:j+1][::-1]:
#             pal_list[i][j] = 1
# for _ in range(int(input())):
#     s, e = map(int, input().split())
#     print(pal_list[s-1][e-1])




# 1)
# n = int(input())
# nums = list(map(chr, input().split()))
# chars = "".join([chr(num) for num in nums])
# for _ in range(int(input())):
#     s, e = map(int, input().split())
#     print(1 if chars[s-1:e] == chars[s-1:e][::-1] else 0)
