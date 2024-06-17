#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    ans = []
    counter = defaultdict(int)
    for course_size in course:
        for order in orders:
            val = list(combinations(sorted(order), course_size)) #모든 combination을 저장
            for combination in val:
                counter["".join(combination)] += 1 #각 combin마다 카운터+=1

    arr = []
    for k, v in counter.items():
        if v >= 2:
            arr.append((v,k)) #조합이 2번 이상 등장한 값만 저장

    for course_size in course: #course_size마다 최대빈도 조합을 찾는다.
        cmax = 0
        temp = []

        for n, s in arr:
            if len(s) == course_size:
                if n > cmax:
                    cmax = n
                    temp = [s]
                elif n == cmax:
                    temp.append(s)
        for t in temp:
            ans.append(t)

    return sorted(ans)


