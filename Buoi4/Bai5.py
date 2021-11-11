
# Em tham khảo bài bạn Nam, vì em chưa hiểu đầu bài cho lắm, em sẽ fix lại sau
a = input()
Max = 0;
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a.count(a[i:j]) > 1:
            Max = max(Max,j-i+1)
print(Max)