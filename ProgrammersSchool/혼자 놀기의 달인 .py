#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

def solution(cards):
    groups = []
    visited = set()

    def dfs(idx): #recursion을 통해 부모를 찾는다.
        group.add(idx)
        if cards[idx]-1 not in visited:
            visited.add(cards[idx]-1)
            dfs(cards[idx]-1)

    for idx in range(len(cards)):
        if idx in visited:
            continue
        visited.add(idx)
        group = set()
        dfs(idx)
        groups.append(len(group))

    if len(groups) == 1:
        return 0
    else:
        groups.sort(reverse=True)
        return groups[0] * groups[1]