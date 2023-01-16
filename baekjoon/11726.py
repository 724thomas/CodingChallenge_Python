# https://www.acmicpc.net/problem/11726

'''
1. 아이디어 :
    1) dp문제인것 같다. 6번째까지 그려보니 패턴이 보인다. 결국에 가짓수는 피보나치 수열이다.
2. 시간복잡도 :
    1) O(n)
3. 자료구조 :
    1) 배열
'''
import sys
# nums = list(map(int, input().split()))
n = int(sys.stdin.readline())
dp = {}
dp[1] = 1
dp[2] = 2
for i in range(3, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]
print(dp[n] % 10007)
