s = input()
s = s.lower()
a = set()
for i in s:
    if i=='p' or i=='a' or i=='n' or i=='g' or i=='r' or i=='m':
        a.add(i)
print(a)
p = str(a)
print(len(p))
if len(p)==30:
    print("YES")
else:
    print('NO')