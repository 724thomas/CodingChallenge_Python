#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        ans=[]
        temp=[]
        for i in range(len(score)):
            temp.append(score[i][k])
        temp.sort(reverse=True)
        for num in temp:
            for s in score:
                if num in s:
                    ans.append(s)
                    break
        return ans
