# https://www.acmicpc.net/problem/15577

'''
1. 아이디어 :
    1) 힙으로 정렬하여 출력
2. 시간복잡도 :
    1) O(n) + O(k) * O(logn) = O(n)
        입력받는 횟수 +  heapify 정렬 * Heappush, Heappoop
3. 자료구조 :
    1) 힙
'''
import heapq
import sys
input = sys.stdin.readline

n = int(input())
math_scores =[int(input()) for x in range(n)]
heapq.heapify(math_scores)

ans = heapq.heappop(math_scores)
for i in range(n-1):
    ans = (ans + heapq.heappop(math_scores))/2

print("{:.6f}".format(ans))