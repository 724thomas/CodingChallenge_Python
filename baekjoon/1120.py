# https://www.acmicpc.net/problem/1120

'''
1. 아이디어 :
    슬라이딩 윈도우
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(s1, s2):
    ans = []
    for i in range(len(s2)-len(s1)+1):
        temp = 0
        for j in range(len(s1)):
            if s1[j] != s2[i+j]:
                temp += 1
        ans.append(temp)

    return min(ans)

n, m = list(map(str, input().strip().split()))
print(solution(n, m))


# http://colorscripter.com/s/7VI79Dt