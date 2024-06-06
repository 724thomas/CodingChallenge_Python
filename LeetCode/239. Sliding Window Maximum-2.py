#

'''
1. 아이디어 :
ㅤㅤmonotonic stack을 이용하여 풀 수 있다.
    1. 초기 k개의 원소를 스택에 넣어준다.
    2. 스택의 맨 앞 원소가 최대값이다.
    3. 새로운 원소가 들어올 때마다 스택의 맨 뒤 원소부터 비교하여 최대값을 갱신한다.
    4. 슬라이딩 윈도우의 범위를 벗어난 원소를 스택에서 제거한다.
    5. 스택의 맨 앞 원소가 최대값이다.
    6. 최대값을 ans에 저장한다.
    7. ans를 반환한다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    큐
'''


from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = deque()


        for i in range(k):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

        ans.append(nums[queue[0]])

        for i in range(k, len(nums)):
            while queue and queue[0] <= i-k:
                queue.popleft()

            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            ans.append(nums[queue[0]])
        return ans