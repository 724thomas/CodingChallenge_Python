#https://leetcode.com/problems/binary-watch/description/

'''
1. 아이디어 :
    비트로 생각하면 쉬운걸 너무 어렵게 접근했었다.
2. 시간복잡도 :
    O(2^10)
    키고(1) 끄고(0) 를 10번 반복한다.
3. 자료구조 :
    배열
'''


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        lights = ["0"]*10 #비트를 저장하기 위한 배열

        def backtracking(start, on_count):
            if on_count == turnedOn: #몇개가 켜져있는지 sum을 사용하지 않고 on_count 변수로 트래킹한다.
                hour = int("".join(lights[:4]),2) #앞에 4개를 비트에서 숫자로 변환
                minute = int("".join(lights[4:]),2) #뒤에 6개를 비트에서 숫자로 변환
                if hour < 12 and minute < 60: #0~11시, 0~59분이 맞는지 체크한다.
                    ans.append(f"{hour}:{minute:02d}")
                return

            for i in range(start, 10):
                lights[i] = "1"
                backtracking(i+1, on_count+1)
                lights[i] = "0"

        backtracking(0, 0)
        return ans