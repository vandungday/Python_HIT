# Hàm kiểm tra số đó phải là số may mắn hay không
def kt(n):
    tong = 0
    for i in range(1, n):
        if (n % i) == 0:
            tong += i
    if tong > n:
        return True
    else:
        return False

n = int(input())
a = list(map(int, input().split()))
b= []
print(a)
for i in a:
    if kt(i):
        b.append(i)
b.sort()
print(len(b), b)
