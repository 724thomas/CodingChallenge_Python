# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


import sys
input = sys.stdin.readline

'''
(0,0)
(1,1)
(0,1)
(2,2)
(1,2)
(0,2)
(3,3)
(2,3)
(1,3)
(0,3)


'''
def solution():
    n = int(input())
    arr = [int(x) for x in input().split()]
    alist = [[0 for _ in range(n)] for _ in range(n)]
    print(*alist, sep = "\n")
    for j in range(1, n):
        for i in range(j-1,-1,-1):
            current_min = sys.maxsize
            for k in range(j-i):
                current_min = min(current_min, alist[i][i+k] + alist[i+k+1][j])
            alist[i][j] = current_min + sum(arr[i:j+1])
    print(*alist, sep = "\n")
'''
(0,4) // i=0, j=4
current_min = min(current_min, alist[i][i+k] + alist[i+k+1][j])

current_min = min(current_min, alist[0][0] + alist[1][5])
current_min = min(current_min, alist[0][1] + alist[2][5])
current_min = min(current_min, alist[0][2] + alist[3][5])
current_min = min(current_min, alist[0][3] + alist[4][5])
current_min = min(current_min, alist[0][4] + alist[5][5])

current_min = min(current_min, (A~A) + (B~F))
current_min = min(current_min, (A~B) + (C~F))
current_min = min(current_min, (A~C) + (D~F))
current_min = min(current_min, (A~D) + (E~F))
current_min = min(current_min, (A~E) + (F~F))

'''

for i in range(500):
    if 2**i-2 >= 200000000:
        print(i)
        break

