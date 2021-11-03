from functools import reduce


# Nguồn code từ bạn Phan Nhật Thắng (Vũ Phong)
def xd10(x: str) -> bool:
    '''
        input: 1 chuỗi cần ktra
    :return:
        đúng thì true, sai thì false
    '''

    return '1' in x or '0' in x

def ss10(x: str, y: str) -> bool:
    '''
        input: 2 chuỗi cần so sánh
    :return:
        2 so nếu tương đương -> true
        còn nếu không -> false
    '''
    a = ''
    for i in range(len(x)):
        if x[i] == '1' or x[i] == '0':
            a += str(i + 1)

    b = ''
    for i in range(len(y)):
        if y[i] == '1' or y[i] == '0':
            b += str(i + 1)

    return a == b

def is10(s: str) -> str:
    a = ''
    for i in range(len(s)):
        if s[i] == '1' or s[i] == '0':
            a += str(i + 1)

    return a

def count10(a: list()) -> int:
    ans = set()
    for i in a:
        if is10(i):
            ans.add(is10(i))
    return len(ans)

a = list(map(str, input().split()))
print(count10(a))
