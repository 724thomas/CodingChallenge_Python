# https://www.acmicpc.net/problem/10816 숫자 카드 2

'''
1. 아이디어 :
    해시맵
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    해시맵
'''
from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

int(input().rstrip())
integer_list = [int(num) for num in input().split()]
hmap = defaultdict(int)
for n in integer_list:
    hmap[n] += 1
int(input().rstrip())
integer_list = [int(num) for num in input().split()]
for i in range(len(integer_list)):
    integer_list[i] = hmap[integer_list[i]]
print(*integer_list)
