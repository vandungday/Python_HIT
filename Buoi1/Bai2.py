import math
# F(x) = (x^2 + e^x + sin(x)) / sqrt(x^2+1)
x = float(input('Nhap x = '))
f = (x**2 + math.e**x + math.sin(x) )/ math.sqrt(x*x+1)
print('F(x) = ', f)
