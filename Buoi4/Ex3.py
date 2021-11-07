a = [1,2,3,4,5]
b=[]
for i in range(len(a)):
    if a[i]%2!=0:
        b.append(i)
for i in a:
    if i%2!=0:
        a.remove(i)
print(b)
print(a)