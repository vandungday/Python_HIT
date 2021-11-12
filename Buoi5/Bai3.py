
def check(n):
    count =0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==3:
        return True
    else:
        return False
n = int(input())
a = list(map(int, input().split()))
count = 0 
for i in a:
    if check(i):
        count +=1
if count==0:
    print('KHÔNG')
else:
    print(count)