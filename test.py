d = {
    'a': 1,
    'b': 1,
}

print(d.get('a'))
f = d.get('c')

if f:
    print('True')
else:
    print('False')