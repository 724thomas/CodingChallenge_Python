# https://www.acmicpc.net/problem/5568

'''
1. 아이디어 :
    중복되는 숫자가 들어있을 수 있기때문에 visited안에 인덱스를 두었다.
    visited에 인덱스를 넣고 빼면서 백트래킹을 수행한다.
2. 시간복잡도 :
    O(n!)
3. 자료구조 :
    해시셋
'''

n = int(input())
k = int(input())
cards = [input() for _ in range(n)]

ans = set()
visited = set()


def bt(s):
    if len(visited) == k:
        ans.add(s)
        return

    for i in range(len(cards)):
        if i not in visited:
            visited.add(i)
            bt(s + cards[i])
            visited.remove(i)

bt("")
print(len(ans))
