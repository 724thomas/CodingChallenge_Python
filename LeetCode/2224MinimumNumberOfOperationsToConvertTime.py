#https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        h=abs((int(current[:2])-int(correct[:2]))*60+(int(current[3:])-int(correct[3:])))

        return h//60+(h%60)//15+((h%60)%15)//5+(((h%60)%15)%5)