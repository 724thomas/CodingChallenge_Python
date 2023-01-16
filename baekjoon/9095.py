# https://www.acmicpc.net/problem/9095
import sys
input = sys.stdin.readline
# dp = {0: 0, 1: 1, 2: 2, 3: 4}
# for j in range(int(input())):
#     n = int(sys.stdin.readline())
#     if n in dp:
#         print(dp[n])
#     else:
#         for i in range(4, n + 1):
#             dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
#         print(dp[n])

def recursive(data):
    if (data == 1):
        return 1
    elif (data == 2):
        return 2
    elif (data == 3):
        return 4
    else:
        return recursive(data - 1) + recursive(data - 2) + recursive(data - 3)
for _ in range((int(input()))):
    print(recursive(int(input())))



'''
1=1
2=11/2 2
3=2+1 111/12/21/3 4
4=1111/112/121/211/22/13/31 7
5=11111/2111/1211/1121/1112/221/212/122/311/131/113/32/23 13



'''
