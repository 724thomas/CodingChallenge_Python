#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        target=1
        while target<=n:
            if target==n:
                return True
            else:
                target*=4
        return False