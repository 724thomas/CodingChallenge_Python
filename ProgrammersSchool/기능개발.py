# https://school.programmers.co.kr/learn/courses/30/lessons/42586
'''
1. 아이디어 :
    1) math.ceil을 이용하여 남은 일수를 계산하며 current max에 따라 count를 증가시킨다.
2. 시간복잡도 :
    1) O(n)
    - for문을 돌면서 조건문 확인
3. 자료구조 :
    1) 배열
'''
import math


def solution(progresses, speeds):
    answer, cmax, count = [], math.ceil((100 - progresses[0]) / speeds[0]), 1
    for i in range(1, len(progresses)):
        if math.ceil((100 - progresses[i]) / speeds[i]) <= cmax:
            count += 1
        else:
            answer.append(count)
            cmax, count = math.ceil((100 - progresses[i]) / speeds[i]), 1
    answer.append(count)
    return answer
