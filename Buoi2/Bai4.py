import string
s = input()
while len(s)>10:
    print('Nhập lại: ')
    s = input()
# a
print(s[2:7])
# b
print(s.upper())
print(s.lower())
print(s.replace('b', 'g'))
# c
a = 'hElLo-mY-NAMe-iS-SuZIe'
print(a.title().replace('-',' '))