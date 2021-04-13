import sys
sys.stdin = open('input2.txt', 'r')

h2b = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111',
}

code_dict = {
    3211: '0',
    2221: '1',
    2122: '2',
    1411: '3',
    1132: '4',
    1231: '5',
    1114: '6',
    1312: '7',
    1213: '8',
    3112: '9',
}


def f(n, m):
    s = 0
    for i in range(n):
        for j in range(m):
            p = [0] * 8
            for k in range(8):
                cnt = [0] * 4
                while bit[i][j] == 0:
                    cnt[0] += 1
                    j += 1
                
                while bit[i][j]:
                    cnt[1] += 1
                    j += 1
                
                while bit[i][j] == 0:
                    cnt[2] += 1
                    j += 1

                while bit[i][j]:
                    cnt[2] += 1
                    j += 1

                x = min(cnt)
                for y in range(3):
                    cnt[y] //= x
                
                ratio = cnt[0]*1000 + cnt[1]*100 + cnt[2]*10 + cnt[3]
                p[k] = code_dict.get(ratio)

                if 

        


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    code = [list(input()) for _ in range(n)]
    bit = [[0] * (m * 4) for _ in range(n)]

    for i in range(n):
        for j in range(m):
            bit[i][j*4+0] = int(h2b[code[i][j]][0])
            bit[i][j*4+1] = int(h2b[code[i][j]][1])
            bit[i][j*4+2] = int(h2b[code[i][j]][2])
            bit[i][j*4+3] = int(h2b[code[i][j]][3])
    
    print(bit)