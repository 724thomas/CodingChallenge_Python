# https://www.acmicpc.net/problem/10815 숫자 카드

'''
1. 아이디어 :

2. 시간복잡도 :
    O(n)
3. 자료구조 :

'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

int(input().rstrip())
integer_set = set([int(num) for num in input().split()])
int(input().rstrip())
check_list = [int(num) for num in input().split()]
for i in range(len(check_list)):
    check_list[i] = 1 if check_list[i] in integer_set else 0
print(*check_list)

