#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            if not stack:
                stack.append(n)
            else:
                while k and stack and stack[-1] > n:
                    stack.pop()
                    k-=1
                stack.append(n)
            # print(stack)

        stack = stack[:len(stack)-k]
        ans = "".join(stack)
        idx = 0
        for i in range(len(ans)):
            if ans[i] != '0':
                break
            idx+=1
        ans = ans[idx:]
        return ans if ans else "0"
