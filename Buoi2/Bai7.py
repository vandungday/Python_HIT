n = int(input('Nhập n: '))
ten=[]
dantoc=[]
t=[]
maxn=0
for i in range(n):
    s=input().split()
    ten.append(s[0])
    dantoc.append(s[1])

for i in range(len(dantoc)):
    if dantoc.count(dantoc[i])>maxn:
        maxn=dantoc.count(dantoc[i])
        s=dantoc[i]
        print(s)
for i in range(len(ten)):
    if dantoc[i]==s:
        t.append(ten[i])
print(ten)