#https://leetcode.com/problems/longest-repeating-character-replacement/description/?source=submission-ac

'''
1. 아이디어 :
    투 포인터로, left와 right를 초기화한다
    l과 r 구간 길이 - 가장 많이 나오는 문자의 개수 > k 이면 l을 한칸 이동하고,
    그렇지 않으면 r을 한칸 이동한다.
    r이 끝에 닿으면 종료한다.
2. 시간복잡도 :
    O(26*n)
3. 자료구조 :
    해시맵
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        ans = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)

            while (r-l+1) - max(count.values()) > k:
                count[s[l]]-=1
                l+=1
            ans = max(ans, r-l+1)

        return ans