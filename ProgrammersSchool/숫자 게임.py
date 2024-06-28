#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


def solution(A, B):
    A.sort()
    B.sort()
    ap = 0
    wins = 0
    for n in B:
        if n > A[ap]:
            wins += 1
            ap += 1

    return wins
