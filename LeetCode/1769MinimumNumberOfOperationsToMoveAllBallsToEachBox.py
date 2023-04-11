#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans=[0 for x in range(len(boxes))]

        for i in range(len(ans)):
            for j in range(i,len(ans)):
                if i!=j:
                    if boxes[j]=="1":
                        ans[i]+=j-i

        for i in range(len(ans)-1,-1,-1):
            for j in range(i-1,-1,-1):
                if i!=j:
                    if boxes[j]=="1":
                        ans[i]+=i-j
        return ans