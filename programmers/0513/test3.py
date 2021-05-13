s = ['1110', '100111100', '0111111010']
answer = []

for _s in s:
    number = _s
    number_length = len(number)

    if number_length < 4:
        answer.append(number)
    else:
        res = ''
        flag = False
        while True:
            try:
                idx_110 = number.index('110')
                
                number = number[:idx_110] + number[idx_110+3:]
                tmp = number[3:]
                len_number = len(number)
                if len_number == 1:
                    if number == '1':
                        res += '1101'
                    else:
                        res += '0110'
                    flag = True
                    break
                elif len_number == 2:
                    if number == '11':
                        res += '11011'
                    elif number == '10':
                        res += '10110'
                    elif number == '00':
                        res += '00110'
                    elif number == '01':
                        res += '01101'
                    flag = True
                    break
                else:  # 3개 이상 남았을 때
                    tmp_3 = number[:3]
                    if tmp_3 == '111':
                        res += '110'
                        number = '111' + tmp
                    elif tmp_3 == '011':
                        res += '011'
                        number = '011' + tmp
                    elif tmp_3 == '101':
                        res += '101'
                        number = '101' + tmp
                    elif tmp_3 == '001':
                        res += '001'
                        number = '101' + tmp
                    elif tmp_3 == '100':
                        res += '100'
                        number = tmp + '110'
                    elif tmp_3 == '010':
                        res += '010'
                        number = tmp + '110'
                    elif tmp_3 == '000':
                        res += '000'
                        number = tmp + '110'
                    elif len_number == 3 and tmp_3 == '110':
                        res += '110'
                        break
                    elif tmp_3 == '110':
                        number = tmp + '110'

            except:
                res += number
                flag = True
                break
        if not flag:
            res += number
        answer.append(res)

print(answer)
        