# https://school.programmers.co.kr/learn/courses/30/lessons/81303

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Node:
    def __init__(self, idx):
        self.prev = None
        self.next = None
        self.idx = idx  # 노드의 인덱스를 저장

def solution(n, k, cmd):
    node_arr = [Node(i) for i in range(n)]
    for i in range(1, n):
        node_arr[i - 1].next = node_arr[i]
        node_arr[i].prev = node_arr[i - 1]

    deleted_nodes = []
    curr_node = node_arr[k]
    head = node_arr[0]  # head 노드 초기화

    for c in cmd:
        if c[0] == "U":
            x = int(c[2:])
            for _ in range(x):
                curr_node = curr_node.prev
        elif c[0] == "D":
            x = int(c[2:])
            for _ in range(x):
                curr_node = curr_node.next
        elif c[0] == "C":
            deleted_nodes.append(curr_node)
            if curr_node.prev:
                curr_node.prev.next = curr_node.next
            else:  # 현재 노드가 head일 경우
                head = curr_node.next
            if curr_node.next:
                curr_node.next.prev = curr_node.prev
            curr_node = curr_node.next if curr_node.next else curr_node.prev
        elif c[0] == "Z":
            node_to_restore = deleted_nodes.pop()
            if node_to_restore.prev:
                node_to_restore.prev.next = node_to_restore
            else:  # 복구되는 노드가 head가 될 경우
                head = node_to_restore
            if node_to_restore.next:
                node_to_restore.next.prev = node_to_restore

    # 최종 상태 생성
    result = ["X"] * n
    curr = head
    while curr:
        result[curr.idx] = "O"
        curr = curr.next

    return "".join(result)