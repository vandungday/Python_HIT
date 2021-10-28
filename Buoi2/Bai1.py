
s1 = input('Nhập chuỗi: ')
s2 = 'TRẺTRÂU'
i = 0
for c in s1:
    if i==len(s2):
        break
    elif c==s2[i]:
        i+=1
if i==len(s2):
    print('TRẺ TRÂU')
else:
    print('KHÔNG TRẺ TRÂU')
