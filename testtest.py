import sys
sys.stdin = open('input2.txt', 'r')
 
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
 

def solution(_code):
    global res

    # 16진수 코드 -> 10진수 -> 2진수
    _code = int(_code, 16)
    _code = format(_code, 'b')

    # 16진수 코드를 유효한 2진수로 변환
    _code = make_binary_str(_code)

    # 2진수 코드를 비율로 변환
    _code = make_code_ratio(_code)
    
    # 10진수 코드로 변환
    try:
        _code = make_code(_code)
        
        # 암호 검증
        res += isCode(_code)
        return True
    except:
        return False

 
T = int(input())
 
for tc in range(1, T+1):
    n, m = map(int, input().split())
    li = [input() for _ in range(n)]
    res = 0
    # 암호 코드 찾기
    for i in range(n):
        if li[i] != '0' * m:  # 빈 열이 아니면
            for j in range(m):
                if li[i][j] != '0':  # 0이 아닌 것을 만나면
                    k = j + 11
                    code = li[i][j:k]
                    if solution(code):  # 예외가 터지지 않으면
                        # j ~ k-1 이 같을 때까지 모든 열을 0으로 초기화
                        tmp_i = i
                        while tmp_i < n:
                            if li[tmp_i][j:k] == code:
                                for l in range(j, k):
                                    _li[tmp_i][l] = '0'
                            else:
                                break
                    else:  # 예외가 터지면
                        k += 1
    
    print(f'#{tc} {res}')

 