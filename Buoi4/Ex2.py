s = 'jenny'
n = len(s)
if len(s)>=2:
    b = s[0:2] + s[n-2:n]
else:
    b = ''
print(b)