#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def get_score(string, score):
            stack = []
            for c in s:
                if stack and stack[-1] == string[0] and c == string[1]:
                    stack.pop()
                    ans[0] += score
                else:
                    stack.append(c)
            return "".join(stack)

        ans = [0]
        if x > y:
            s = get_score("ab", x)
            s = get_score("ba", y)
        else:
            s = get_score("ba", y)
            s = get_score("ab", x)
        return ans[0]