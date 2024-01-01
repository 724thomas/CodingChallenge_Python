# https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75

'''
1. 아이디어 :
    문제를 잘못 이해하고 스택으로 풀려했었다.
    투 포인터로 풀 수 있다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    배열
'''

class Solution:
    def compress(self, chars):
        write_idx, move_idx = 0, 0

        while move_idx < len(chars):
            current_char = chars[move_idx] # 해당 알파벳
            count = 0 # 갯수 카운트

            while move_idx < len(chars) and chars[move_idx] == current_char:
                count += 1
                move_idx += 1

            # move_idx는 다음 다른 알파벳에 위치
            # count는 해당 알파벳의 갯수가 저장

            chars[write_idx] = current_char
            write_idx += 1

            # 배열의 idx에 해당 알파벳 저장 후, 다음 저장 자리에 위치

            if count > 1:
                for digit in str(count):
                    chars[write_idx] = digit
                    write_idx += 1

            # 다음 저장 자리부터 count가 2 이상일때, str(count)의 자리수 만큼 작성되고, 포인터가 움직인다.

        return write_idx

        # write_idx 위치가 정답. (write_idx는 0부터 시작했기 때문)