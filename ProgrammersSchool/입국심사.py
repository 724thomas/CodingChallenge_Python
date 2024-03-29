# https://school.programmers.co.kr/learn/courses/30/lessons/43238

'''
1. 아이디어 :
    1) (시간 초과)배열 [0] * len(times)를 만들어 놓고, 제일 작은 값의 해당 times[i] 값을 추가하고,
    그 다음 작은 값의 해당 times[i] 값을 추가하는 식으로 n=0일때까지 연산 후, 마지막에 넣었던 index를 리턴한다.
    2) 총 걸리는 시간을 기준으로 이분탐색을 한다.
2. 시간복잡도 :
    1) O(n) * O(n) = O(n^2)
    -  min을 구하는 시간, 각 배열에 값을 추가해보는 시간
    2) O(logN)
3. 자료구조 :
    1) 배열
    2) Binary Search
'''


import sys
input = sys.stdin.readline

def solution(n, times):
    left, right = 1, n*max(times)
    while left < right:
        mid = (left+right)//2
        if sum([mid//t for t in times]) < n:
            left = mid+1
        else:
            right = mid
    return left
'''
left, right, mid
1, 60, 30
sum = 30//7=4 + 30//10=3 = 7 < 6
1, 31, 16
sum = 16//7=2 + 16//10=1 = 3 < 6
17, 31, 24
sum = 24//7=3 + 24//10=2 = 5 < 6
25, 31, 28
sum = 28//7=4 + 28//10=2 = 6 < 6
25, 29, 27
sum = 27//7=3 + 27//10=2 = 5 < 6
28, 29, 28
sum = 28//7=4 + 28//10=2 = 6 < 6
28, 28, 28



'''

