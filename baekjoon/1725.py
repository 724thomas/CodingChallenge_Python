# https://www.acmicpc.net/problem/1725

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

graph = []
for i in range(int(input())):
    graph.append(int(input()))

max_area = 0
graphs = [graph]

while len(graphs) >= 1:
    graph = graphs.pop()
    cmin = min(graph)
    max_area = max(max_area, len(graph) * cmin)

    temp = []
    for n in graph:
        if n == cmin:
            if temp:
                graphs.append(temp)
                temp = []
        else:
            temp.append(n)
    if temp:
        graphs.append(temp)
print(max_area)
