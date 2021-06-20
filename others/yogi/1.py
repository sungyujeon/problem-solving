
# '; ' 기준으로 분할
# Original Name 저장
# Name 분할 / if len(Name) > 2 Name[1,3] else Name[1,2]
# last hyphen 처리 >> 8개까지
# email 형식 처리 >> email 저장(중복 처리)
# 출력 형식

S = 'John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker'
C = 'Example'

original_names = S.split('; ')
C = C.lower()
N = len(original_names)
email_dict = {}

def make_email(name, company, e_dict):
    name = name.replace('-', '')
    tmp_name_list = name.split()
    
    first_name = tmp_name_list[0]
    last_name = tmp_name_list[1] if len(tmp_name_list) < 3 else tmp_name_list[-1]
    last_name = last_name[:8]

    first_name = first_name.lower()
    last_name = last_name.lower()
    

    email = f'{first_name}.{last_name}@{company}.com'
    
    # 중복 체크
    if email in e_dict:
        e_dict[email] += 1
        cnt = e_dict.get(email)
        email = f'{first_name}.{last_name}{cnt}@{company}.com'
    else:
        e_dict[email] = 1

    return email

def formatting(name, email):
    my_form = f'{name} <{email}>'
    return my_form

for i in range(N):
    email = make_email(original_names[i], C, email_dict)
    original_names[i] = formatting(original_names[i], email)

res = '; '.join(original_names)
print(res)
    