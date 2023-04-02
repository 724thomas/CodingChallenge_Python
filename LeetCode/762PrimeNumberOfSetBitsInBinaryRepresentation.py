#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes={2,3,5,7,11,13,17,19}
        ans=0
        for i in range(left, right+1):
            if bin(i)[2:].count("1") in primes:
                ans+=1
        return ans