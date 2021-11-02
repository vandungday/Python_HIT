
def xd10(x: int) -> bool:
    if '1' in str(x) or '0' in str(x):
        return True

    return False
# em không biết làm bài này hic hic hic
def ss10(x: list):
    s = []
    for i in x:
        if xd10(i)==True:
            s.append(i)
    return s
    
print(ss10({100, 200, 322}))
