# https://www.acmicpc.net/problem/2343 기타 레슨

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''
import sys

sys.setrecursionlimit(1000000)


def solution(blueray, time_list):
    if len(time_list) == 1:
        return time_list[0]

    def check(n):

        counts = 1
        temp = 0
        for time in time_list:
            if temp + time > n:
                counts += 1
                temp = time
            else:
                temp += time
        return counts <= blueray

    left = max(time_list)
    right = sum(time_list)
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left


courses, blueray = list(map(int, input().split()))
time_list = [int(num) for num in input().split()]
print(solution(blueray, time_list))
