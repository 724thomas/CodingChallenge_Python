# https://school.programmers.co.kr/learn/courses/30/lessons/178871 달리기 경주

'''
1. 아이디어 :
    해시맵으로 플레이어의 순위를 기록.
    이름이 불릴때마다, 해당 플레이어와 앞에있는 플레이어의 순서를 바꿔주고, 해시맵 값을 갱신
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    해시맵
'''

def solution(players, callings):
    hmap = {players[i] : i for i in range(len(players))}

    for curr_name in callings:
        curr_rank = hmap[curr_name]
        prev_name = players[curr_rank-1]
        prev_rank = hmap[prev_name]

        players[curr_rank], players[prev_rank] = players[prev_rank], players[curr_rank]
        hmap[curr_name] -= 1
        hmap[prev_name] += 1

    return players