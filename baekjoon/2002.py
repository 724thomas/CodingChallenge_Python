# https://www.acmicpc.net/problem/2002

'''
1. 아이디어 :
    나온 차량의 인덱스를 처음 들어갔을때와 확인한다. (잘 이해 안됨)
2. 시간복잡도 :
    O(n*2)
3. 자료구조 :
    배열, 해시맵
'''

n = int(input())
start = {}
end = []
for i in range(n):
    start[input()] = i
for i in range(n):
    end.append(input())

count = 0
for i in range(n-1):
    for j in range(i+1, n):
        if start[end[i]] > start[end[j]]:
            count+=1
            break

print(count)