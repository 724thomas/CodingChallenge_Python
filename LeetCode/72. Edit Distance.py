#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp={}

        def dfs(i, j):
            if i == len(word1): #word1의 index가 끝까지 갔을때,
                return len(word2) - j #word2의 길이 - word2의 index
            if j == len(word2): #word2의 index가 끝까지 갔을때,
                return len(word1) - i #word1의 길이 - word1의 index

            if (i,j) in dp:
                return dp[(i,j)]

            if word1[i] == word2[j]: #word1, word2의 index에 있는 char이 같을때
                dp[(i,j)] = dfs(i+1, j+1) #다음 index로 넘어간다.
            else:
                dp[(i,j)] = 1 + min(
                    dfs(i, j+1), # insert
                    dfs(i+1, j), # delete
                    dfs(i+1, j+1)) #change

            return dp[(i,j)]

        return dfs(0,0)