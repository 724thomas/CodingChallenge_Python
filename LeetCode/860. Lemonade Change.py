#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = defaultdict(int)

        for bill in bills:
            changes[bill] += 1
            if bill == 10:
                if changes[5] == 0:
                    return False
                changes[5] -= 1
            elif bill == 20:
                if changes[10] >= 1 and changes[5] >= 1:
                    changes[10] -=1
                    changes[5] -=1
                elif changes[5] >= 3:
                    changes[5] -= 3
                else:
                    return False
        return True