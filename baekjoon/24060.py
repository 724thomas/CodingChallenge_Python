# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''
import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()


def solution(n, m, arr):
    # print(*arr, sep="\n")

    counter = []

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = (len(arr)+1) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        lp = rp = 0
        new_arr = []
        while lp < len(left) and rp < len(right):
            if left[lp] <= right[rp]:
                new_arr.append(left[lp])
                counter.append(left[lp])
                lp += 1
            else:
                new_arr.append(right[rp])
                counter.append(right[rp])
                rp += 1

        while lp < len(left):
            new_arr.append(left[lp])
            counter.append(left[lp])
            lp += 1
        while rp < len(right):
            new_arr.append(right[rp])
            counter.append(right[rp])
            rp += 1

        return new_arr

    merge_sort(arr)
    return counter[m - 1] if m <= len(counter) else -1


if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    print(solution(n, m, arr))