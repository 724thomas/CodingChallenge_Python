# https://leetcode.com/problems/3sum-smaller/
'''
1. 아이디어 :
    1) 2중 포문안에, num1을 고정시키고, 투포인터로 num2, num3을 찾는다. num3를 감소시키다가
    num2 + num3 < target - num1 이 되는 순간, break를 걸고 rp와 lp의 거리를 ans에 더해준다.
2. 시간복잡도 :
    1) O(logn) + O(n^2) * O(logN)= O(n^2logN)
    - sort * 2중포문 * 투포인터
3. 자료구조 :
    1) 배열

'''
class Solution:
    def threeSumSmaller(self, n: List[int], target: int) -> int:
        ans=0
        n.sort()
        for j in range(len(n)-2):
            t=target-n[j]
            rp=len(n)-1
            for i in range(j+1,len(n)-1):
                lp=i
                while lp<rp:
                    if n[lp]+n[rp]>=t:
                        rp-=1
                    elif n[lp]+n[rp]<t:
                        print(j,lp,rp)
                        ans+=rp-lp
                        break

        return ans