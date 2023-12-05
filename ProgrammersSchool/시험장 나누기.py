#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

from collections import defaultdict
from collections import deque
import heapq

from heapq import heappush, heappop
from collections import defaultdict
from math import inf

def solution(n, start, end, roads, traps):
    traps = set(traps)

    # 아래와 같은 entry들로 Adjacency list를 구성합니다.
    # (이웃 노드, cost, 뒤집혔을 때 유효한 edge인지 여부)
    A = defaultdict(list)
    for u, v, w in roads:
        A[u].append( (v, w, False) )
        A[v].append( (u, w, True) )
    print(A)

    # 다익스트라를 시도해봅니다.
    flipped = [False] * (n+1)  # 함정 노드가 뒤집혔는지 나타내는 flag입니다.
    q = [(0, start, flipped)]

    # 어떤 노드의 상태는 (노드 번호, 그 노드가 뒤집혔는지, 그 노드의 이웃이 뒤집혔는지) 여부로
    # 유일하게 결정됩니다.
    start_state = ( start, False, tuple([False] * len(A[start])) )
    dist = {}; dist[start_state] = 0
    while q:
        d, u, flipped = heappop(q)

        u_state = ( u, flipped[u], tuple(flipped[v] for v, _, _ in A[u]) )
        if d > dist.get(u_state, inf):
            continue

        for v, w, valid_when_flipped in A[u]:
            # u-v edge가 뒤집혔는지 아닌지 판단합니다.
            # 노드 u, v 둘다 안 뒤집혔거나, 둘다 뒤집혔다면 edge는 그대로입니다.
            edge_flipped = flipped[u] ^ flipped[v]

            # valid_when_flipped이 False이면,
            # u, v 둘다 안 뒤집혔거나, 둘다 뒤집혔을 때만 유효한 edge입니다.
            # valid_when_flipped이 True이면,
            # u, v 둘 중 하나만 뒤집혔을 때만 유효한 edge입니다.
            if (valid_when_flipped is False and not edge_flipped) or \
                    (valid_when_flipped is True and edge_flipped):

                f = flipped[:]
                if v in traps:
                    f[v] = not f[v]

                v_state = ( v, f[v], tuple(flipped[x] for x, _, _ in A[v]) )

                if d + w < dist.get(v_state, inf):
                    dist[v_state] = d + w
                    heappush( q, (d+w, v, f) )

    candidates = [dist[k] for k in dist if k[0] == end]
    return min(candidates)

print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2]))
print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2,3]))