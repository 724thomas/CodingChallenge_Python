# https://www.acmicpc.net/problem/1065

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n):

    def check(num):
        if len(num) <= 2:
            return True
        else:
            d = int(num[1]) - int(num[0])
            for i in range(2, len(num)):
                if int(num[i]) - int(num[i-1]) != d:
                    return False
            return True

    ans = 0
    for i in range(1, n+1):
        if check(str(i)):
            ans += 1



    return ans


n = int(input().rstrip())
print(solution(n))
