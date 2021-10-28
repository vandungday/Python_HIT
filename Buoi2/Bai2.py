
aList = list(map(int, input().split()))
print(aList)
result = aList
for i in range(1,len(aList)):
    result[i] = result[i-1] + result[i]
print(result)