# https://www.acmicpc.net/problem/27172

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''
from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline




def solution(arr):
    dict = defaultdict(int)
    for i, n in enumerate(arr):
        dict[n] = i
    scores = [0] * len(arr)
    cmax = max(arr)

    for i, n in enumerate(arr):
        temp = n * 2
        while temp <= cmax:
            if temp in dict:
                scores[i] += 1
                scores[dict[temp]] -=1
            temp += n
    return scores




input()
arr = list(map(int, input().strip().split()))
print(*solution(arr))


