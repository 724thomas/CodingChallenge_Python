# https://leetcode.com/problems/task-scheduler/description/

'''
1. 아이디어 :
    1)  Heap을 이용하여 가장 많이 사용되는 알파벳의 개수를 Counter로 구한다.
        스택 배열과 time 변수를 만들어서, while문을 돌려가면서 가장 많이 사용된 알파벳을 스택에 넣는다.
        스택에 넣을 때마다 time을 1씩 증가시키고, 스택의 길이가 n보다 작을 때까지 스택에 넣는다.
        스택의 길이가 n이 되면, 스택의 길이만큼 time을 증가시키고, 스택을 비운다.
        스택을 비울 때마다, 가장 많이 사용된 알파벳의 개수를 1씩 감소시킨다.
        가장 많이 사용된 알파벳의 개수가 0이 되면, 다음으로 많이 사용된 알파벳을 스택에 넣는다.
        힙과 스택에 값이 없으면, time을 리턴한다.
2. 시간복잡도 :
    1) O(n) + O(time) = O(n)
    - n개의 원소를 넣고 빼는 작업 + time만큼의 while 작업
3. 자료구조 :
    1) Heap, Stack
'''


from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        tasks = []
        stack = deque()
        for key,val in c.items():
            tasks.append(-val)
        heapq.heapify(tasks)
        print(tasks)

        t=0
        while tasks or stack:
            if tasks:
                num = -heapq.heappop(tasks)
                num -= 1
                if num !=0:
                    stack.append([num,t+n])

            while stack and stack[0][1]==t:
                num = -stack.popleft()[0]
                heapq.heappush(tasks,num)
            t+=1
        return t

