# https://www.acmicpc.net/problem/10811 바구니 뒤집기

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = list(map(int, input().split()))

ans = [i for i in range(1, n+1)]
for i in range(m):
    left, right = list(map(int, input().split()))
    for j in range(((right-left)//2)+1):
        ans[left+j-1], ans[right-j-1] = ans[right-j-1], ans[left+j-1]

print(*ans)
