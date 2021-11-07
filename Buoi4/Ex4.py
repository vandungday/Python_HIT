''''
Bài 4 : Viết một hàm nhập vào 1 list n số nguyên.
 Sau đó viết 1 hàm đếm số lần xuất hiện của các số có trong mảng. 
 Cuối cùng viết hàm in ra theo format a(số xuất hiện trong mảng) : b (số số lần xuất hiện của số a trong mảng) ….. 
(Chú ý là viết hàm chứ ko phải dùng hàm nhé )
'''
def dem(a, pos):
    count=0
    for i in a:
        if i == pos:
            count = count + 1
    return(count) 

n = int(input())
a = list(map(int, input().split()))
for i in set(a):
    print(i, ":", dem(a,i))