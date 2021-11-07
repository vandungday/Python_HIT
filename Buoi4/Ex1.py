s = "abcde"
n = int(input())
a= s[:n]
index = len(s) 
while index > n: 
    a += s[ index - 1 ] 
    index = index - 1 
print(a) 
