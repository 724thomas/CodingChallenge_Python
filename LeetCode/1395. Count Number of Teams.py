#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def numTeams(self, rating: List[int]) -> int:

        ans = 0
        for mid in range(1, len(rating)-1):
            left_smaller = right_larger = 0
            for i in range(mid):
                if rating[i] < rating[mid]:
                    left_smaller += 1
            for i in range(mid+1, len(rating)):
                if rating[i] > rating[mid]:
                    right_larger += 1
            ans += left_smaller * right_larger


            left_larger = mid - left_smaller
            right_smaller = len(rating) - mid - 1 - right_larger
            ans += left_larger * right_smaller

        return ans