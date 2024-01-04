# https://www.acmicpc.net/problem/7568 덩치

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(people):
    ans = []
    for x1, y1 in people:
        rank = 1
        for x2, y2 in people:
            if x1 < x2 and y1 < y2:
                rank += 1
        ans.append(rank)
    return ans


n = int(input().rstrip())
integer_list = [list(map(int, input().split())) for _ in range(n)]
print(*solution(integer_list))
