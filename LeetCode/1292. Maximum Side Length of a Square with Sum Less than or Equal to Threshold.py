#

'''
1. 아이디어 :
    dp로 풀 수 있다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열
'''



class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        ans=0
        matrix=[[0 for i in range(len(mat[0])+1)] for j in range(len(mat)+1)]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):

                matrix[i][j]= mat[i-1][j-1] + matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]
                cmin=min(i,j)-1

                if i > ans and j > ans:
                    val = matrix[i][j] - matrix[i-ans-1][j] - matrix[i][j-ans-1] + matrix[i-ans-1][j-ans-1]
                    if val<=threshold:
                        ans += 1

        return ans
