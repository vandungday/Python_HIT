a = list(map(int, input('Nhập mảng: ').split()))
k = int(input('Nhập k: '))
count = 0;
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==k:
            # print(a[i],a[j])
            count+=1;
print(count)