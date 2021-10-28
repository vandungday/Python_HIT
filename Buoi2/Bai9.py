a = list(map(int, input().split()))
b = []
c = []
for i in range(len(a)):
    if i%2==0:
        b.append(a[i])
    else:
        c.append(a[i])
a = b+c
print(a)