def stringToNumber(_s):
    dic = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    return dic.get(_s)

def solution(s):
    answer = ''
    front = 0
    while True:
        if front >= len(s):
            break

        num = s[front]
        if num.isdigit():
            answer += num
            front += 1
        else:
            i = 3
            while True:
                res = stringToNumber(s[front:front+i])
                if res != None:
                    if (res.isdigit()):
                        answer += res
                        front += i
                        break
                else:
                    if i >= len(s):
                        break
                    i += 1
        
    return answer

s = 'one4seveneight'
print(solution(s))
