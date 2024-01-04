# https://www.acmicpc.net/problem/10818

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
int(input().rstrip())
integer_list = [int(num) for num in input().split()]
print(min(integer_list), max(integer_list))

