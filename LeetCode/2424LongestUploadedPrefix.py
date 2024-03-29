# https://leetcode.com/problems/longest-uploaded-prefix/description/

'''
1. 아이디어 :
    1)  (시간초과)배열안에 False로 채워넣고, upload할 때마다 True로 바꾼다.
        longest 호출시, True가 아닌 첫번째 인덱스를 찾아서 반환한다.
    2)  배열안에 False로 채워넣고(n+1개), upload할 때마다 True로 바꾼다.
        longest 호출시마다 최대값을 저장하고, 호출시마다 최대값부터 탐색을 시작한다.
2. 시간복잡도 :
    1)  O(1) , O(1) , O(k) * O(n)
        upload, longest, k번 longest 호출 * 배열 탐색
    2)  O(1), O(1), O(k) * O(n-k)
        upload, longest, k번 longest 호출 * 배열 탐색(최대값부터)
3. 자료구조 :
    1) 배열
    2) 배열
'''


#1)
class LUPrefix:

    def __init__(self, n: int):
        self.upload_list = [False for x in range(n)]

    def upload(self, video: int) -> None:
        self.upload_list[video-1] = True

    def longest(self) -> int:
        for i in range(len(self.upload_list)):
            if not self.upload_list[i]:
                return i
        return len(self.upload_list)


#2)
class LUPrefix:

    def __init__(self, n: int):
        self.upload_list = [False for x in range(n+1)]
        self.cmax = 0

    def upload(self, video: int) -> None:
        self.upload_list[video-1] = True

    def longest(self) -> int:
        while self.upload_list[self.cmax]:
            self.cmax+=1
        return self.cmax

