# https://www.acmicpc.net/problem/1620 나는야 포켓몬 마스터 이다솜

'''
1. 아이디어 :

2. 시간복잡도 :
    O( n )
3. 자료구조 :

'''
from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


n, m = list(map(int, input().split()))

nums = defaultdict(str)
names = defaultdict(int)

for i in range(n):
    name = input().rstrip()
    nums[i+1] = name
    names[name] = i+1

for _ in range(m):
    guess = input().rstrip()
    if guess.isdigit():
        print(nums[int(guess)])
    else:
        print(names[guess])
