#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = lasers = 0
        for i in range(len(bank)):
            ones=bank[i].count("1")
            if ones!=0:
                lasers+=prev*ones
                prev=ones
        return lasers