#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import random
import bisect
from typing import List

class Solution:
    def __init__(self, w: List[int]):
        # 누적합 배열 생성
        self.prefix_sums = [0]
        for weight in w:
            self.prefix_sums.append(self.prefix_sums[-1] + weight)

    def pickIndex(self) -> int:
        # 1부터 self.total_sum 사이의 랜덤 값 생성
        target = random.randint(1, self.prefix_sums[-1])
        # 이분 탐색을 이용해 target이 위치한 인덱스 찾기
        index = bisect.bisect_left(self.prefix_sums, target)
        return index -1
