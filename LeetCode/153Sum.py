#https://leetcode.com/problems/3sum/description/
'''
1. 아이디어 :
    1) for문으로 num1을 target으로 지정하고, 나머지를 투 포인터로 확인한다.
2. 시간복잡도 :
    1) O(n) * O(nlogn) = O(n^2 * logn)
    - num1타겟을 for문으로 돌고((n) * 나머지를 투포인터로 돌고(n) * 정렬(logn)
3. 자료구조 :
    1) 배열
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numset = sorted(nums)
        print(numset)
        ans = []
        for i in range(len(numset)-2):
            lp = i+1
            rp = len(numset)-1
            target = 0 - numset[i]
            temp = []
            while lp<rp:
                if numset[lp]+numset[rp] == target:
                    if [numset[i],numset[lp],numset[rp]] not in ans:
                        ans.append([numset[i],numset[lp],numset[rp]])
                    lp+=1
                    rp-=1
                elif numset[lp]+numset[rp] > target:
                    rp-=1
                elif numset[lp]+numset[rp] < target:
                    lp+=1
        return ans

