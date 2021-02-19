# 백준 2941번 S5
# 크로아티아 알파벳

import sys

input = sys.stdin.readline


def count_word(_word):
    new_word = ''
    i = 0
    while i < len(_word):
        if i < len(_word)-1:
            if _word[i] == 'c':
                if _word[i+1] in ['=', '-']:
                    new_word += _word[i]
                    i += 1
                else:
                    new_word += _word[i]
            elif _word[i] in ['l', 'n']:
                if _word[i+1] == 'j':
                    new_word += _word[i]
                    i += 1
                else:
                    new_word += _word[i]
            elif _word[i] in ['s', 'z']:
                if _word[i+1] == '=':
                    new_word += _word[i]
                    i +=1
                else:
                    new_word += _word[i]
            elif _word[i] == 'd':
                if _word[i+1] == '-':
                    new_word += _word[i]
                    i += 1
                elif i < len(_word)-2 and _word[i+1] == 'z' and _word[i+2] == '=':
                    new_word += _word[i]
                    i += 2
                else:
                    new_word += _word[i]
            else:
                new_word += _word[i]
        else:
            new_word += _word[i]
        
        i += 1

    return len(new_word)

words = input().rstrip()
print(count_word(words))


# def count_word(_word):
#     new_word = ''
#     i = 0
#     while i < len(_word):
#         if i < len(_word) - 1:
#             if _word[i] in ['c', 's', 'z']:
#                 if _word[i+1] in ['=', '-']:
#                     new_word += _word[i]
#                     i += 1
#             elif _word[i] in ['l', 'n']:
#                 if _word[i+1] == 'j':
#                     new_word += _word[i]
#                     i += 1
#                 else:
#                     new_word += _word[i]
#             elif _word[i] == 'd':
#                 if i < len(_word)-2: # dz= 검사
#                     if _word[i+1] == 'z' and _word[i+2] == '=':
#                         new_word += _word[i]
#                         i += 2
#                     else:
#                         if _word[i+1] == '-':
#                             new_word += _word[i]
#                             i += 1
#                         else:
#                             new_word += _word[i]    
#                 else:  # d- 검사
#                     if _word[i+1] == '-':
#                         new_word += _word[i]
#                         i += 1
#                     else:
#                         new_word += _word[i]
#             else:
#                 new_word += _word[i]
#         else:
#             new_word += _word[i]
        
#         i += 1
    
#     return len(new_word)



# words = input().rstrip()
# print(count_word(words))
