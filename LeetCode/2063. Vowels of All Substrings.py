#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def countVowels(self, word: str) -> int:
        count = 0
        d = {'a':1,'e':1,'i':1,'o':1,'u':1}

        for i in range(len(word)):
            if word[i] in d:
                count += (len(word)-i)*(i+1)
        return count