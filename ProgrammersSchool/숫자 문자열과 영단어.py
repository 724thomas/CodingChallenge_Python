#https://school.programmers.co.kr/learn/courses/30/lessons/81301

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

def solution(s):
    adict={"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6,
           "seven":7, "eight":8, "nine":9}
    for key in adict.keys():
        s=s.replace(key,str(adict[key]))
    return int(s)