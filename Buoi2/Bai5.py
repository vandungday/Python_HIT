
a = int(input('Nhập a: '))
while a>9:
    s = 0
    while(a>0):
        s += a %10
        a = a//10
    a = s
print(s)