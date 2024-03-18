#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        n_set = set()
        n_set.add(amount)
        step = 1
        visited = set()

        while n_set:
            new_set = set()
            for target in n_set:
                for coin in coins:
                    new_amount = target - coin
                    if new_amount == 0:
                        return step
                    if new_amount in visited or new_amount < 0:
                        continue
                    new_set.add(new_amount)
                    visited.add(new_amount)
            n_set = new_set
            step+=1
        return -1
