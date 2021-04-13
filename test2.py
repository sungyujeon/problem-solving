import sys
sys.stdin = open('input.txt', 'r')


def find_code(_li, _n, _m):
    code_set = set()
    for i in range(_n):
        tmp_code = _li[i]
        if tmp_code:
            tmp_code = tmp_code.split('000000')
            for c in tmp_code:
                if c:
                    code_set.add(c.strip('0'))
    return code_set
 
def make_binary_str(code_str):
    l = len(code_str)
    last_idx = 0
    for i in range(l-1, -1, -1):
        if code_str[i] == '1':
            last_idx = i
            break
    code_str = code_str[:last_idx+1]
    
    # 앞에 56의 배수가 되도록 0 추가
    l = len(code_str)
    if l % 56:  # 56의 배수가 아니면
        cnt = 0
        while l % 56:
            l += 1
            cnt += 1
        code_str = ('0' * cnt) + code_str
    return code_str


def make_code_ratio(code_str):
    l = len(code_str)
    multiples = l // 56
    code_ratio = [0] * 32
    
    flag = '1'
    flag_idx = 31
    for i in range(l-1, 0, -1):
        code_ratio[flag_idx] += 1
        if code_str[i-1] != flag:
            flag = '0' if flag == '1' else '1'
            flag_idx -= 1
    code_ratio[0] += 1  # 1번 idx까지 추가하였으므로 0번 idx 하나 추가
    
    # multiples로 나누어 비율로 표시
    code_ratio = list(map(lambda x: str(x // multiples), code_ratio))
    return code_ratio

def make_code(_code_ratio):
    code_dict = {
        '3211': '0',
        '2221': '1',
        '2122': '2',
        '1411': '3',
        '1132': '4',
        '1231': '5',
        '1114': '6',
        '1312': '7',
        '1213': '8',
        '3112': '9',
    }

    res = ''
    for i in range(0, 29, 4):
        code_num =  _code_ratio[i] + _code_ratio[i+1] + _code_ratio[i+2] + _code_ratio[i+3]
        if code_dict.get(code_num) is not None:
            res += code_dict[code_num]
            
    return res
 
 
def isCode(code_str):
    total = 0
    for i in range(8):
        if i % 2:
            total += int(code_str[i])
        else:
            total += (int(code_str[i]) * 3)

    if total % 10:
        return 0
    else:
        _res = 0
        for i in range(8):
            _res += int(code_str[i])
        return _res
 
 
T = int(input())
 
for tc in range(1, T+1):
    n, m = map(int, input().split())
    li = [input() for _ in range(n)]

    # 암호 코드 찾기
    code_set = find_code(li, n, m)
    
    res = 0
    for code in code_set:
        # 16진수 코드 -> 10진수 -> 2진수
        code = int(code, 16)
        code = format(code, 'b')

        # 16진수 코드를 유효한 2진수로 변환
        code = make_binary_str(code)

        # 2진수 코드를 비율로 변환
        code = make_code_ratio(code)
        
        # 10진수 코드로 변환
        code = make_code(code)

        # 암호 검증
        res += isCode(code)
    
    print(f'#{tc} {res}')

 