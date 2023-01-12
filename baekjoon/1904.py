# https://www.acmicpc.net/problem/1904

'''
1. 아이디어 :
    1) dp문제인것 같다. 6번째까지 그려보니 패턴이 보인다. 결국에 가짓수는 피보나치 수열이다.
    메모리 제한이 256MB이므로, 1,000,000까지의 피보나치 수열을 구할 수 없다.
    case는 하나이고, 몇번째인지만 출력하면 되므로, a,b = b, a+b를 사용한다.
2. 시간복잡도 :
    1) O(n)
3. 자료구조 :
    1) -
'''

import sys

input = sys.stdin.readline
a, b = 1, 2
for i in range(int(input())-1):
    a, b = b%15746, (a + b)%15746
print(a)

