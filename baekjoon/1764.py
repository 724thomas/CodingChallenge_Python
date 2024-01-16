# https://www.acmicpc.net/problem/1764 듣보잡

'''
1. 아이디어 :

2. 시간복잡도 :
    O( n )
3. 자료구조 :

'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = list(map(int, input().split()))

seen = set()

for _ in range(n):
    seen.add(input().rstrip())

ans = []
for _ in range(m):
    name = input().rstrip()
    if name in seen:
        ans.append(name)

print(len(ans))
ans.sort()
for n in ans:
    print(n)
