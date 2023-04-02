#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        order={}
        for i in range(len(keyboard)):
            order[keyboard[i]]=i

        ans=abs(0-order[word[0]])
        for i in range(len(word)-1):
            ans+=abs(order[word[i]]-order[word[i+1]])
        return ans