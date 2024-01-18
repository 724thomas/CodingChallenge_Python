# https://www.acmicpc.net/problem/11004

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = list(map(int, input().split()))
integer_list = [int(num) for num in input().split()]



def solution(nums, k):
    return sorted(nums)[k-1]

print(solution(integer_list, m))
