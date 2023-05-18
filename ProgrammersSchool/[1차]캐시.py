# https://school.programmers.co.kr/learn/courses/30/lessons/17680

'''
1. 아이디어 :
    Deque를 사용하여 캐시를 구현한다.
2. 시간복잡도 :
    O(N)
3. 자료구조 :
    Deque
'''

from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    if len(cities) == 0:
        return 0

    cache = deque()
    access_time = 0
    city_list = [city.lower() for city in cities]
    for city in city_list:
        if city in cache:
            access_time += 1
            cache.remove(city)
            cache.append(city)
        else:
            access_time += 5
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city)
    return access_time