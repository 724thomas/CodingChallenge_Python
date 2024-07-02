# https://www.acmicpc.net/problem/9242

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(arr):

    dict = {
        tuple(['***', '* *', '* *', '* *', '***']): "0",
        tuple(['  *', '  *', '  *', '  *', '  *']): "1",
        tuple(['***', '  *', '***', '*  ', '***']): "2",
        tuple(['***', '  *', '***', '  *', '***']): "3",
        tuple(['* *', '* *', '***', '  *', '  *']): "4",
        tuple(['***', '*  ', '***', '  *', '***']): "5",
        tuple(['***', '*  ', '***', '* *', '***']): "6",
        tuple(['***', '  *', '  *', '  *', '  *']): "7",
        tuple(['***', '* *', '***', '* *', '***']): "8",
        tuple(['***', '* *', '***', '  *', '***']): "9"
    }

    num = ""
    for col in range(len(arr[0])):
        temp = []
        for row in range(len(arr)):
            temp.append(arr[row][col][0])
        temp = tuple(temp)
        if temp not in dict:
            return "BOOM!!"
        num += dict[temp]
    return "BEER!!" if int(num) % 6 == 0 else "BOOM!!"


arr = []
for _ in range(5):
    a = list(input())
    temp = []
    try :
        for i in range(0, len(a)-1, 4):
            temp.append([a[i] + a[i + 1] + a[i + 2]])
        arr.append(temp)
    except :
        print("BOOM!!")
        exit()
print(solution(arr))
