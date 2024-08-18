#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        c = sorted([[v,k] for k, v in c.items()], reverse=True)

        ans = 0
        for i in range(len(c)):
            value, key = c[i]
            ans += (int(i // 8) + 1) * value
        return ans
