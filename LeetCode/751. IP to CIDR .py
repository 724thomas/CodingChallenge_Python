# https://leetcode.com/problems/ip-to-cidr/description/

'''
1. 아이디어 :
    - 스택을 사용한다.
    - while문을 통해 ip의 binary, cidr을 매번 저장하고, 마지막 두번째 원소 ip의 cidr번째 숫자가 같으면 해당 cidr을 1 차감한다.
2. 시간복잡도 :
    O(n) * 4
3. 자료구조 :
    스택
'''
class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:

        def ip_to_bin(string_ip, n):
            string_ip = list(map(int, string_ip.split('.')))
            for i in range(3, -1, -1):
                n, string_ip[i] = divmod(string_ip[i] + n, 256)
                if n == 0:
                    break

            bin_ip = []
            for s in string_ip:
                to_bin = bin(int(s))[2:]
                bin_ip.append("0" * (8-len(to_bin)) + to_bin)
            return "".join(bin_ip)

        def bin_to_ip(string_ip, cidr):
            ans = ""
            string_ip = str(string_ip) + "0" * (32-len(string_ip))
            for i in range(4):
                ans += str(int(string_ip[(i+0)*8:(i+1)*8],2)) + "."

            return ans[:-1] + "/" + str(cidr)


        ans = [[ip_to_bin(ip, 0),32]]

        for i in range(1,n):
            ans.append([ip_to_bin(ip,i),32])

            prev_last_bin = ans[-2][0][int(ans[-2][1])-2]
            curr_last_bin = ans[-1][0][int(ans[-2][1])-2]

            while prev_last_bin == curr_last_bin and ans[-2][1] == ans[-1][1]:
                try:
                    ans.pop()
                    ans[-1][1] -= 1

                    prev_last_bin = ans[-2][0][int(ans[-2][1])-2]
                    curr_last_bin = ans[-1][0][int(ans[-2][1])-2]
                except:
                    break

        ans = [bin_to_ip(ans_ip,ans_cidr) for ans_ip, ans_cidr in ans]
        return ans








