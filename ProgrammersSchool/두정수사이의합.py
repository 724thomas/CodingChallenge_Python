#https://school.programmers.co.kr/learn/courses/30/lessons/12912?language=python3

def solution(a, b):
    return sum(x for x in range(min(a,b),max(a,b)+1))