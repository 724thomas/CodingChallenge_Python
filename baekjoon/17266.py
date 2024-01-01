# https://www.acmicpc.net/problem/17266 어두운 굴다리

'''
1. 아이디어 :
    이분탐색을 사용한다.
    최소한의 높이를 구해야하기때문에, left < right를 사용하고,
    조건문이 True가 나오는 다음 값을 리턴한다.
2. 시간복잡도 :
    O(NlogD)
3. 자료구조 :
    배열
'''
import sys

sys.setrecursionlimit(1000000)

input = sys.stdin.readline

distance = int(input().rstrip())
lights_count = int(input().rstrip())
lights_pos = [int(num) for num in input().split()]


def solution(distance, lights_count, lights_pos):
    def find_end(radius):
        start = 0
        for light in lights_pos:
            lmin = light - radius
            lmax = light + radius
            if lmin <= start:
                start = lmax
            else:
                return False
        if start < distance:
            return False
        return True

    left = 0
    right = distance

    while left < right:
        mid = (left + right) // 2
        if find_end(mid):
            right = mid
        else:
            left = mid + 1
    return left


print(solution(distance, lights_count, lights_pos))
