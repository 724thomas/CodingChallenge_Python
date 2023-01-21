#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''
iplist = []
for _ in range(int(input())):
    ip = input()
    ip = ip.split('/')
    iplist.append("".join(['{:08b}'.format(int(x)) for x in ip[0].split('.')]))
for i in iplist:
    print(i)
