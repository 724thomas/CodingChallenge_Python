# https://www.acmicpc.net/problem/13164

'''
1. 아이디어 :
    차이를 정렬한다.
    가장 큰 m-1개의 차이를 선택하여 그룹으로 나눈다.
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    배열
'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n, m, arr):
    diff = sorted([arr[i+1]-arr[i] for i in range(len(arr)-1)])
    return sum(diff[:-m+1]) if m > 1 else sum(diff)

n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
print(solution(n, m, arr))


