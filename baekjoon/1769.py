# https://www.acmicpc.net/problem/1769

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = str(input().rstrip())
count = 0

while len(n) != 1:
    temp = 0
    for num in n:
        temp += int(num)
    n = str(temp)
    count += 1

print(count)
print("YES" if n in ("3", "6", "9") else "NO")
