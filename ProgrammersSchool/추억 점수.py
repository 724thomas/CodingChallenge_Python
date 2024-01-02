# https://school.programmers.co.kr/learn/courses/30/lessons/176963 추억점수

'''
1. 아이디어 :
    해시맵 사용
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    해시맵
'''

from collections import defaultdict
def solution(name, yearning, photo):
    hmap = defaultdict(int)
    for i in range(len(name)):
        hmap[name[i]] = yearning[i]

    ans = []
    for people in photo:
        score = 0
        for person in people:
            score += hmap[person]
        ans.append(score)


    return ans