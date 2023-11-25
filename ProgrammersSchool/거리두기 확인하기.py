# https://school.programmers.co.kr/learn/courses/30/lessons/81302

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

from collections import deque

def solution(places):

    def dfs(row, col, distance, place_idx):
        if row<0 or row>=len(place) or col<0 or col>=len(place[0]) or distance>2 or (row,col) in visited or place[row][col]=="X":
            return

        if place[row][col]=="P":
            print(row,col, distance)
            ans[place_idx]=0

        visited.add((row,col))
        for row2, col2 in dir:
            nrow = row+row2
            ncol = col+col2
            if (nrow, ncol) not in visited:
                dfs(nrow,ncol,distance+1, place_idx)

    dir = [ [0,1], [0,-1], [-1,0], [1,0] ]
    ans = [1] * len(places)
    for place_idx in range(len(places)):
        place = places[place_idx]
        for i in range(len(place)):
            place[i] = [c for c in place[i]]
        visited=set()

        for row in range(len(place)):
            for col in range(len(place[0])):
                if place[row][col] == "P":
                    place[row][col] = "A"
                    dfs(row,col,0, place_idx)
                    place[row][col] = "P"
    return ans


