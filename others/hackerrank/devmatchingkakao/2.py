# hackerrank 카카오엔터 2번
# IP Address Validation

import re

def validateAddress(addresses):
    def isValid(addr):

        pattern4 = '^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$'
        match = re.match(pattern4, addr)
        if match:
            flag = True
            nums = addr.split('.')
            for num in nums:
                try:
                    if int(num) > 7:
                        if num[0] == '0' or int(num) > 255:
                            flag = False
                except:
                    flag = False
            
            if not flag:
                return False
            
            return 4

        pattern6 = '^[0-9a-f]{1,4}$'
        addr = addr.split(':')
        cnt = 0
        zero = False
        for _addr in addr:
            if _addr == '':  # 공백
                cnt += 1
                zero = True
            else:
                match = re.match(pattern6, _addr)
                if match:
                    cnt += 1
                else:
                    return False
        if cnt > 8:
            return False
        else:
            if not zero:
                return False
            return 6
    
    n = len(addresses)
    res = [None] * n
    for k in range(n):
        flag = isValid(addresses[k])

        if not flag:
            res[k] = 'Neither'
        else:
            res[k] = f'IPv{flag}'
    
    return res


# addresses = ['121.18.19.20', '0.12.12.34', '121.234.12.12', '23.45.12.56', '0.1.2.3']
addresses = ['2001:db8::ff00:42:8329', '::1']
# addresses = ['000.012.234.23', '666.666.23.23', '.213.123.23.32', '23.45.22.32.', '272:2624:235e:3bc2:c46d:682:5d46:638g', '1:22:333:4444']
print(validateAddress(addresses))