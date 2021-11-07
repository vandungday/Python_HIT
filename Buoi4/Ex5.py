
'''
Bài 5 : Viết một hàm nhập một mảng, 1 số x từ bàn phím. 
Viết một hàm xóa số x đầu tiên tìm được ra khỏi mảng và in vị trí của số x đầu tiên.
Viết một hàm xóa tất cả số x ra khỏi mảng
Nhập một số y từ bàn phím. Viết 1 hàm kiểm tra rồi chèn x vào trị trí y.
'''


def Nhap():
    n = int(input())
    a = list(map(int, input().split()))
    return a
def Tim(a: list,x:int):
    temp = 0
    for i in range(len(a)):
        if a[i]==x:
            temp = i
            a.remove(a[i])
            break
    print(f'Mang sau khi xoa so {x} dau tien la: {a}')
    print(f'Vi tri so {x} dau tien la: {temp}')

def Xoa(a: list, x: int):
    while x in a:
        a.remove(x)
    print(f'Mang sau khi xoa cac so {x} la: {a}')

def Chen(a:list, x:int, y: int):
    if x<0 or x >= len(a):
        print('Khong chen duoc')
    else:
        a.insert(x, y)
    print(f'Mang sau khi chen so {y} vao vi tri {x} cua mang a la: {a}')
a= Nhap()
print(a)
Tim(a,3)
Xoa(a,1)
Chen(a,0,8)