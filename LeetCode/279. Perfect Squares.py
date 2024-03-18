#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def numSquares(self, n: int) -> int:
        nset = set()
        nset.add(n)
        step = 1

        while nset:
            new_set = set()
            for n in nset:
                for i in range(1, int(sqrt(n))+1):
                    new_n = n - i*i
                    if new_n == 0:
                        return step
                    new_set.add(new_n)
            nset = new_set
            step+=1