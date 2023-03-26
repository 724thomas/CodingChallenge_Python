#https://leetcode.com/problems/flood-fill/description/

'''
1. 아이디어 :
    dfs로 풀 수 있다.
2. 시간복잡도 :
    O(m*n)
3. 자료구조 :
    리스트, 해시셋
'''


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r=len(image)
        c=len(image[0])

        target=image[sr][sc]


        visited=set()
        def dfs(x,y):
            if x<0 or y<0 or x==r or y==c or (x,y) in visited or image[x][y]!=target:
                return

            visited.add((x,y))
            image[x][y]=color

            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)

        dfs(sr,sc)

        return image