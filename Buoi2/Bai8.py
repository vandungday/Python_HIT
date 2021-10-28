s = input('Nhập chuỗi: ')
count = 0
for i in range(len(s)):
    if s[i]=='1':
        count+=1
print(count)
if count%2!=0:
    print('NO')
else:
    index = 0
    sum = count//2;
    for i in range(len(s)):
        if sum==0:
            break
        if s[i] =='1':
            sum-=1
            index = int(i)
    print(s[0:index+1] +" " + s[index+1:len(s)])

