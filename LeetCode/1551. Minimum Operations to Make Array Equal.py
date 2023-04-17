#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def minOperations(self, n: int) -> int:
        return sum([x for x in range(0,n,2)]) if n%2==1 else sum([x for x in range(1,n,2)])