import sys
sys.stdin = open('input.txt', 'r')
from datetime import date

def isCorrect(file):
    file_size = file[0]
    year, month, day = map(int, file[1].split('-'))
    file_date = date(year, month, day)
    file_name = file[2]

    # size
    if not file_size.isdigit():
        unit = file_size[-1]
        if unit == 'G':
            return False
        elif unit == 'M':
            file_size = int(file_size[:-1])
            if file_size >= 14:
                return False

    # date
    std_date = date(1990, 1, 31)
    if std_date >= file_date:
        return False
    
    # name
    lastChar = file_name[-1]
    if lastChar != '~':
        return False
    
    # length == dot_idx
    dot_idx = file_name.index('.')
    return dot_idx


def solution(S):
    file_infos = S.strip().split('\n')
    res = 256

    for file_info in file_infos:
        file_length = isCorrect(file_info.split())

        if file_length and file_length < res:
            res = file_length
    
    if res == 256:
        return 'NO FILES'
    
    return res

S = '715K 2009-09-23 system.zip~\n 179K 2013-08-14 to-do-list.xml~\n 645K 2013-06-19 blockbuster.mpeg~\n  536 2010-12-12 notes.html\n 688M 1990-02-11 delete-this.zip~\n  23K 1987-05-24 setup.png~\n 616M 1965-06-06 important.html\n  14M 1992-05-31 crucial-module.java~\n 192K 1990-01-31 very-long-filename.dll~'
print(solution(S))