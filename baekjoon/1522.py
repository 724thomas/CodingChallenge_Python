# https://www.acmicpc.net/problem/1522

'''
1. 아이디어 :
    1) a를 한곳에 몰려면, b를 전부 옮겨야하는데, 이어져있으므로, s+s(최대 길이 1,000)에 b가 몇개인지 카운트를하고 슬라이딩 윈도우로
    한칸씩 옮기면서 그 구간에 옮겨야되는 a가 몇개인지 카운트를 하며 current min을 갱신한다.
2. 시간복잡도 :
    1) O(n)
    - for문
3. 자료구조 :
    1) String
'''

import sys

input = sys.stdin.readline
s = input().strip()
counta, cmin = s.count("a"), len(s)
s=s+s
for n in range(len(s) - counta + 1):
    cmin = min(cmin, s[n:counta + n].count("b"))
    print(s[n:counta + n])
print(cmin)

