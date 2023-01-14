# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    1) (시간초과) H만큼의 배열을 만들고, N만큼 돌면서 count를 센다.
    2) H만큼 돌면서 카운트 하는 방식을 바꿔야될것 같다. 석순, 종유석
    배열을 만들고, 해당 배열 index에 입력이 들어오면 +1 해주고,
    누적합을 통해 두 배열의 합을 구한다. 마지막으로 두 배열을
    index끼리 더해주고, min값과 count값을 출력한다.
2. 시간복잡도 :
    1) O(n) * O(h) = O(nh)
    - 입력 * for문 배열 count+=1
    1) O(n) + O(n) + O(n) = O(n)
    - 입력 + for문 누적합 계산 + for문 배열 더하기
3. 자료구조 :
    1) 배열
'''

import sys
input = sys.stdin.readline
n, h = map(int, input().split())
left = [0] * (h)
right = [0] * (h)
for i in range(n):
    if i % 2 == 0:
        left[int(input())-1] += 1
    else:
        right[h-int(input())] += 1

left_total = right_total = 0
min_count = left_total + right_total

for i in range(len(right)):
    right[i] = right_total + right[i]
    right_total = right[i]
for i in range(len(left)-1,-1,-1):
    left[i] = left_total + left[i]
    left_total = left[i]
ans = [0] * (h)
for i in range(len(left)):
    ans[i] = left[i] + right[i]
print(min(ans),ans.count(min(ans)))


# 1)
# import sys
# input = sys.stdin.readline
# n, h = map(int, input().split())
# arr = [0] * (h)
# for i in range(n):
#     for j in range(int(input())):
#         if i % 2 == 0:
#             arr[j] += 1
#         else:
#             arr[h - j-1] += 1
# print(min(arr), arr.count(min(arr)))