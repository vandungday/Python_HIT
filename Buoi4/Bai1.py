str = input()
str=str.replace("translate","")
str=str.replace("(","")
str=str.replace(","," ")
str=str.replace(")","")
print(str)
# a = str.index('(')
# print(" ".join(str[a+1:len(str)-1].split(",")))