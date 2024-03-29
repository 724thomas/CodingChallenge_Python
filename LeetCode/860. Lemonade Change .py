# https://leetcode.com/problems/lemonade-change/description/

'''
1. 아이디어 :
    10원부터 소모하다가, 5원이 없으면 False
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    해시맵
'''

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = {}
        changes[5] = changes[10] = changes[20] = 0

        for b in bills:
            changes[b]+=1
            if b == 10:
                changes[5] -=1
            elif b == 20:
                if changes[10]>=1:
                    changes[10]-=1
                    changes[5]-=1
                else:
                    changes[5]-=3
            if changes[5] <0:
                return False

        return True