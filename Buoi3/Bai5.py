def MyMathShower(*a):
    tong = 0
    tich = 1
    hieu = a[0]
    for i in a:
        tong+=i
        tich*=i
    for i in range(1,len(a)):
        hieu-=a[i]
    print(tong,' ', tich,' ', hieu)
MyMathShower(10,4,1,1)
MyMathShower(10,20,30,40,0)