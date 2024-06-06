#

'''
1. 아이디어 :
ㅤㅤ투 포인터로 풀 수 있다.
    left와 right를 각각 이동 시키면서 최대값을 갱신
    기타 문자 갯수 = 포인터 길이 - 현재 가장 많은 문자
2. 시간복잡도 :
    O( n )
3. 자료구조 :
ㅤㅤ해시맵
'''


from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict = defaultdict(int)
        ans = 0

        l = 0
        r = 0

        while r < len(s):
            dict[s[r]] += 1

            while r-l+1 - max(dict.values()) > k:
                dict[s[l]]-=1
                l+=1
            r += 1
            ans = max(ans, r-l)
        return ans

