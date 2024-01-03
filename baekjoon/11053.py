# https://www.acmicpc.net/problem/11053 가장 긴 증가하는 부분 수열

'''
1. 아이디어 :
    스택을 사용해서 풀 수 있다
2. 시간복잡도 :
    O(n^2)
3. 자료구조 :
    스택
'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, arr):
    stack = [-1]

    for num in arr:
        if stack[-1] < num:
            stack.append(num)
        else:
            for i in range(1, len(stack)):
                if num <= stack[i]:
                    stack[i] = num
                    break
    return len(stack)-1


n = int(input().rstrip())
integer_list = [int(num) for num in input().split()]
print(solution(n, integer_list))
