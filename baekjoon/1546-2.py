# https://www.acmicpc.net/problem/1546 평균

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline



n = int(input().rstrip())
integer_list = [int(num) for num in input().split()]
max_score = max(integer_list)
total = 0
for i in range(len(integer_list)):
    total += integer_list[i] / max_score * 100
print(total/len(integer_list))
# dp = [[0 for _ in range(n)] for _ in range(n)]
# dp = [[0 for j in range(n)] for i in range(n)]
# grid = [list(input().rstrip()) for _ in range(n)] # "aaa" "bbb"
# grid = list(list(map(int, input().split())) for _ in range(n)) # "0 0 0 0", "0 0 0 0"



