#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict, deque
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        def topo_sort(conditions):
            conditions = set((condition[0], condition[1]) for condition in conditions)
            later = defaultdict(list)
            degrees = defaultdict(int)
            for prev, curr in conditions:
                later[prev].append(curr)
                degrees[curr] += 1

            queue = deque()
            visited = set()
            for node in range(1, k + 1):
                if degrees[node] == 0:
                    queue.append(node)
                    visited.add(node)

            ans = []
            while queue:
                curr = queue.popleft()
                ans.append(curr)
                for nxt in later[curr]:
                    if nxt in visited:
                        return []
                    degrees[nxt] -= 1
                    if degrees[nxt] == 0:
                        visited.add(nxt)
                        queue.append(nxt)

            if len(ans) == k:
                return ans
            else:
                return []

        row_sort, col_sort = topo_sort(rowConditions), topo_sort(colConditions)
        if not row_sort or not col_sort:
            return []

        val_to_row, val_to_col = {n:i for i, n in enumerate(row_sort)}, {n:i for i, n in enumerate(col_sort)}
        ans = [[0] * k for _ in range(k)]
        for num in range(1, k+1):
            r, c = val_to_row[num], val_to_col[num]
            ans[r][c] = num
        return ans



