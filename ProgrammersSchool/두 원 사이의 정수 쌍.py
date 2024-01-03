# https://school.programmers.co.kr/learn/courses/30/lessons/181187

'''
1. 아이디어 :
    math
2. 시간복잡도 :
    O(r2)
3. 자료구조 :
    -
'''

import math
def solution(r1, r2):
    def calc_distance(radius, x):
        return max(0,radius**2 - x**2)**0.5

    counts = 0
    for i in range(1, r2+1):
        min_val = math.floor(calc_distance(r2, i)) - math.ceil(calc_distance(r1, i)) + 1
        counts += min_val
    return counts * 4
