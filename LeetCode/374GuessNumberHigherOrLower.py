#https://leetcode.com/problems/guess-number-higher-or-lower/description/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        cmin=0
        cmax=n
        cmid=(cmin+cmax)//2
        gResult = guess(cmid)
        #for _ in range(5):
        while True:
            if gResult==1:
                cmin=cmid
                cmid=(cmin+cmax+1)//2
            elif gResult==-1:
                cmax=cmid+1
                cmid=(cmin+cmax)//2
            gResult=guess(cmid)
            if gResult==0:
                return (cmid)
            print(cmid,gResult)